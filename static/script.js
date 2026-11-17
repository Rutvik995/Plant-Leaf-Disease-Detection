document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const dropzonePrompt = document.getElementById('dropzonePrompt');
    const previewContainer = document.getElementById('previewContainer');
    const imagePreview = document.getElementById('imagePreview');
    const btnRemove = document.getElementById('btnRemove');
    const btnAnalyze = document.getElementById('btnAnalyze');
    
    // Output DOM Elements
    const emptyResults = document.getElementById('emptyResults');
    const loadingState = document.getElementById('loadingState');
    const activeResults = document.getElementById('activeResults');
    
    const diseaseTitle = document.getElementById('diseaseTitle');
    const plantCategory = document.getElementById('plantCategory');
    const statusPill = document.getElementById('statusPill');
    const statusText = document.getElementById('statusText');
    const severityPill = document.getElementById('severityPill');
    const confidenceNumber = document.getElementById('confidenceNumber');
    const confidenceBar = document.getElementById('confidenceBar');
    
    const symptomsList = document.getElementById('symptomsList');
    const treatmentText = document.getElementById('treatmentText');
    const top5List = document.getElementById('top5List');
    const allClassesList = document.getElementById('allClassesList');
    const btnToggleAll = document.getElementById('btnToggleAll');
    const allClassesWrapper = document.getElementById('allClassesWrapper');
    const specLatency = document.getElementById('specLatency');

    let currentImageData = null;

    // Drag and Drop Events
    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            dropzone.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            dropzone.classList.remove('dragover');
        });
    });

    dropzone.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileSelect(e.target.files[0]);
        }
    });

    btnRemove.addEventListener('click', (e) => {
        e.stopPropagation();
        resetUpload();
    });

    btnToggleAll.addEventListener('click', () => {
        allClassesWrapper.classList.toggle('hidden');
        const isHidden = allClassesWrapper.classList.contains('hidden');
        btnToggleAll.innerHTML = isHidden 
            ? 'Show All 39 Classes <i data-lucide="chevron-down"></i>' 
            : 'Hide Classes <i data-lucide="chevron-up"></i>';
        lucide.createIcons();
    });

    function handleFileSelect(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please select a valid image file (PNG, JPG, JPEG, WEBP).');
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            currentImageData = e.target.result;
            imagePreview.src = currentImageData;
            dropzonePrompt.classList.add('hidden');
            previewContainer.classList.remove('hidden');
            btnAnalyze.disabled = false;
        };
        reader.readAsDataURL(file);
    }

    function resetUpload() {
        fileInput.value = '';
        currentImageData = null;
        imagePreview.src = '';
        previewContainer.classList.add('hidden');
        dropzonePrompt.classList.remove('hidden');
        btnAnalyze.disabled = true;
    }

    // Generate Synthetic Sample Leaf Image via Canvas
    document.querySelectorAll('.btn-sample').forEach(btn => {
        btn.addEventListener('click', () => {
            const sampleType = btn.getAttribute('data-sample');
            generateSampleLeaf(sampleType);
        });
    });

    function generateSampleLeaf(type) {
        const canvas = document.createElement('canvas');
        canvas.width = 160;
        canvas.height = 160;
        const ctx = canvas.getContext('2d');

        // Background soil / studio neutral
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(0, 0, 160, 160);

        // Draw leaf shape
        ctx.save();
        ctx.translate(80, 80);
        ctx.beginPath();

        if (type === 'potato_healthy') {
            ctx.fillStyle = '#15803d'; // Lush green
        } else if (type === 'apple_scab') {
            ctx.fillStyle = '#4d7c0f'; // Dark olive
        } else if (type === 'tomato_blight') {
            ctx.fillStyle = '#3f6212';
        } else {
            ctx.fillStyle = '#65a30d'; // Corn yellow-green
        }

        ctx.ellipse(0, 0, 45, 65, Math.PI / 6, 0, Math.PI * 2);
        ctx.fill();

        // Draw leaf veins
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, -60);
        ctx.lineTo(0, 60);
        ctx.stroke();

        // Disease spots based on type
        if (type === 'apple_scab') {
            ctx.fillStyle = '#27272a'; // Black/olive spots
            for (let i = 0; i < 7; i++) {
                const rx = (Math.random() - 0.5) * 50;
                const ry = (Math.random() - 0.5) * 70;
                const r = 4 + Math.random() * 8;
                ctx.beginPath();
                ctx.arc(rx, ry, r, 0, Math.PI * 2);
                ctx.fill();
            }
        } else if (type === 'tomato_blight') {
            ctx.fillStyle = '#451a03'; // Dark brown blights
            ctx.beginPath();
            ctx.ellipse(-10, -20, 18, 12, 0.4, 0, Math.PI * 2);
            ctx.fill();
            ctx.beginPath();
            ctx.ellipse(15, 20, 22, 14, -0.3, 0, Math.PI * 2);
            ctx.fill();
        } else if (type === 'corn_rust') {
            ctx.fillStyle = '#b45309'; // Rust orange pustules
            for (let i = 0; i < 12; i++) {
                const rx = (Math.random() - 0.5) * 40;
                const ry = (Math.random() - 0.5) * 80;
                ctx.beginPath();
                ctx.arc(rx, ry, 3, 0, Math.PI * 2);
                ctx.fill();
            }
        }
        ctx.restore();

        const sampleDataUrl = canvas.toDataURL('image/png');
        currentImageData = sampleDataUrl;
        imagePreview.src = sampleDataUrl;
        dropzonePrompt.classList.add('hidden');
        previewContainer.classList.remove('hidden');
        btnAnalyze.disabled = false;

        // Auto trigger analysis for smooth UX
        runAnalysis();
    }

    // Analyze Button Click Event
    btnAnalyze.addEventListener('click', runAnalysis);

    async function runAnalysis() {
        if (!currentImageData) return;

        // UI State: Loading
        emptyResults.classList.add('hidden');
        activeResults.classList.add('hidden');
        loadingState.classList.remove('hidden');
        btnAnalyze.disabled = true;

        try {
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ image: currentImageData })
            });

            const data = await response.json();

            if (!data.success) {
                alert('Analysis error: ' + (data.error || 'Unknown error'));
                loadingState.classList.add('hidden');
                emptyResults.classList.remove('hidden');
                btnAnalyze.disabled = false;
                return;
            }

            // Render Prediction Output
            renderResults(data);

        } catch (err) {
            console.error('Fetch error:', err);
            alert('Failed to connect to API server.');
            loadingState.classList.add('hidden');
            emptyResults.classList.remove('hidden');
        } finally {
            btnAnalyze.disabled = false;
        }
    }

    function renderResults(data) {
        const pred = data.prediction;
        const perf = data.performance;

        // Top match header
        diseaseTitle.textContent = pred.name;
        plantCategory.textContent = `Crop Species: ${pred.plant} | Condition: ${pred.condition}`;

        // Status & Severity Pills
        if (pred.status === 'Healthy') {
            statusPill.className = 'status-pill healthy';
            statusText.textContent = 'Healthy Leaf';
            severityPill.textContent = 'No Infection';
            severityPill.style.color = 'var(--emerald)';
        } else {
            statusPill.className = 'status-pill infected';
            statusText.textContent = pred.status;
            severityPill.textContent = `${pred.severity} Severity`;
            severityPill.style.color = pred.severity === 'Critical' || pred.severity === 'High' ? 'var(--rose)' : 'var(--amber)';
        }

        // Confidence progress
        confidenceNumber.textContent = `${pred.confidence_percent}%`;
        confidenceBar.style.width = `${pred.confidence_percent}%`;

        // Symptoms list
        symptomsList.innerHTML = '';
        if (pred.symptoms && pred.symptoms.length > 0) {
            pred.symptoms.forEach(sym => {
                const li = document.createElement('li');
                li.textContent = sym;
                symptomsList.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'No abnormal symptoms observed.';
            symptomsList.appendChild(li);
        }

        // Treatment
        treatmentText.textContent = pred.treatment || 'No special treatment needed.';

        // Top 5 Chart
        top5List.innerHTML = '';
        data.top5_distribution.forEach(item => {
            const row = document.createElement('div');
            row.className = 'prob-row';
            row.innerHTML = `
                <div class="prob-label-line">
                    <span class="prob-name">${item.rank}. ${item.name}</span>
                    <span class="prob-val">${item.probability}%</span>
                </div>
                <div class="prob-bar-track">
                    <div class="prob-bar-fill" style="width: ${item.probability}%;"></div>
                </div>
            `;
            top5List.appendChild(row);
        });

        // All 39 Classes List
        allClassesList.innerHTML = '';
        data.all_classes.forEach(c => {
            const chip = document.createElement('div');
            chip.className = 'class-chip';
            chip.innerHTML = `
                <span>${c.name}</span>
                <strong style="color: var(--cyan);">${c.probability}%</strong>
            `;
            allClassesList.appendChild(chip);
        });

        // Performance Specs
        specLatency.textContent = `${perf.inference_latency_ms} ms`;

        // Switch to Active Results View
        loadingState.classList.add('hidden');
        activeResults.classList.remove('hidden');
        lucide.createIcons();
    }
});
