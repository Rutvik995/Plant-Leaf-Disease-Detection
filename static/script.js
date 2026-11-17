document.addEventListener('DOMContentLoaded', () => {
    // Input & Dropzone Elements
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const dropzonePrompt = document.getElementById('dropzonePrompt');
    const previewContainer = document.getElementById('previewContainer');
    const imagePreview = document.getElementById('imagePreview');
    const scanLaser = document.getElementById('scanLaser');
    const scanningBadge = document.getElementById('scanningBadge');
    const btnRemove = document.getElementById('btnRemove');
    const btnAnalyze = document.getElementById('btnAnalyze');
    const btnClear = document.getElementById('btnClear');

    // Results Display Elements
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
    const diseaseDescription = document.getElementById('diseaseDescription');
    const symptomsList = document.getElementById('symptomsList');
    const treatmentText = document.getElementById('treatmentText');
    const top5List = document.getElementById('top5List');
    const allClassesList = document.getElementById('allClassesList');
    const btnToggleAll = document.getElementById('btnToggleAll');
    const allClassesWrapper = document.getElementById('allClassesWrapper');
    const classSearchInput = document.getElementById('classSearchInput');
    const specLatency = document.getElementById('specLatency');
    const btnPrintReport = document.getElementById('btnPrintReport');

    // Camera Modal Elements
    const btnOpenCam = document.getElementById('btnOpenCam');
    const cameraModal = document.getElementById('cameraModal');
    const cameraBackdrop = document.getElementById('cameraBackdrop');
    const btnCloseCam = document.getElementById('btnCloseCam');
    const btnCancelCam = document.getElementById('btnCancelCam');
    const btnSnapPhoto = document.getElementById('btnSnapPhoto');
    const cameraVideo = document.getElementById('cameraVideo');
    const cameraCanvas = document.getElementById('cameraCanvas');

    let currentImageData = null;
    let cameraStream = null;
    let cachedAllClasses = [];

    // Drag & Drop Handling
    ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropzone.classList.remove('dragover');
        });
    });

    dropzone.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files && files.length > 0) {
            handleFileSelect(files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleFileSelect(e.target.files[0]);
        }
    });

    btnRemove.addEventListener('click', (e) => {
        e.stopPropagation();
        resetUpload();
    });

    btnClear.addEventListener('click', (e) => {
        resetUpload();
    });

    // File selection logic -> Instant Auto-Diagnosis
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
            btnClear.disabled = false;

            // Automatically run diagnosis immediately upon selection!
            runAnalysis();
        };
        reader.readAsDataURL(file);
    }

    function resetUpload() {
        fileInput.value = '';
        currentImageData = null;
        imagePreview.src = '';
        previewContainer.classList.add('hidden');
        dropzonePrompt.classList.remove('hidden');
        scanLaser.classList.add('hidden');
        scanningBadge.classList.add('hidden');
        btnAnalyze.disabled = true;
        btnClear.disabled = true;

        activeResults.classList.add('hidden');
        loadingState.classList.add('hidden');
        emptyResults.classList.remove('hidden');
    }

    // Camera Handlers
    btnOpenCam.addEventListener('click', (e) => {
        e.stopPropagation();
        openCamera();
    });

    [btnCloseCam, btnCancelCam, cameraBackdrop].forEach(elem => {
        elem.addEventListener('click', closeCamera);
    });

    async function openCamera() {
        cameraModal.classList.remove('hidden');
        try {
            cameraStream = await navigator.mediaDevices.getUserMedia({
                video: { facingMode: 'environment', width: { ideal: 640 }, height: { ideal: 640 } },
                audio: false
            });
            cameraVideo.srcObject = cameraStream;
        } catch (err) {
            console.error('Camera access error:', err);
            alert('Unable to access camera. Please check browser permissions or use file upload.');
            closeCamera();
        }
    }

    function closeCamera() {
        if (cameraStream) {
            cameraStream.getTracks().forEach(track => track.stop());
            cameraStream = null;
        }
        cameraVideo.srcObject = null;
        cameraModal.classList.add('hidden');
    }

    btnSnapPhoto.addEventListener('click', () => {
        if (!cameraVideo.videoWidth) return;

        cameraCanvas.width = cameraVideo.videoWidth;
        cameraCanvas.height = cameraVideo.videoHeight;
        const ctx = cameraCanvas.getContext('2d');
        ctx.drawImage(cameraVideo, 0, 0, cameraCanvas.width, cameraCanvas.height);

        const photoData = cameraCanvas.toDataURL('image/jpeg', 0.92);
        currentImageData = photoData;
        imagePreview.src = photoData;
        dropzonePrompt.classList.add('hidden');
        previewContainer.classList.remove('hidden');
        btnAnalyze.disabled = false;
        btnClear.disabled = false;

        closeCamera();

        // Immediately auto-analyze the captured frame
        runAnalysis();
    });

    // Sample Synthetic Leaves for Instant Testing
    document.querySelectorAll('.btn-sample').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const sampleType = btn.getAttribute('data-sample');
            generateSampleLeaf(sampleType);
        });
    });

    function generateSampleLeaf(type) {
        const canvas = document.createElement('canvas');
        canvas.width = 160;
        canvas.height = 160;
        const ctx = canvas.getContext('2d');

        // Background soil tone
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(0, 0, 160, 160);

        ctx.save();
        ctx.translate(80, 80);
        ctx.beginPath();

        if (type === 'potato_healthy') {
            ctx.fillStyle = '#15803d'; // Lush Green
        } else if (type === 'apple_scab') {
            ctx.fillStyle = '#4d7c0f'; // Dark Olive
        } else if (type === 'tomato_blight') {
            ctx.fillStyle = '#3f6212'; // Deep Green/Brown
        } else if (type === 'grape_blackrot') {
            ctx.fillStyle = '#166534'; // Grape green
        } else {
            ctx.fillStyle = '#65a30d'; // Corn yellowish-green
        }

        ctx.ellipse(0, 0, 48, 68, Math.PI / 6, 0, Math.PI * 2);
        ctx.fill();

        // Veins
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.22)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, -62);
        ctx.lineTo(0, 62);
        ctx.stroke();

        // Disease Patterns
        if (type === 'apple_scab') {
            ctx.fillStyle = '#27272a';
            for (let i = 0; i < 9; i++) {
                const rx = (Math.random() - 0.5) * 55;
                const ry = (Math.random() - 0.5) * 75;
                ctx.beginPath();
                ctx.arc(rx, ry, 4 + Math.random() * 7, 0, Math.PI * 2);
                ctx.fill();
            }
        } else if (type === 'tomato_blight') {
            ctx.fillStyle = '#451a03'; // Necrotic brown lesions
            ctx.beginPath();
            ctx.ellipse(-12, -22, 20, 14, 0.4, 0, Math.PI * 2);
            ctx.fill();
            ctx.beginPath();
            ctx.ellipse(16, 24, 24, 16, -0.3, 0, Math.PI * 2);
            ctx.fill();
        } else if (type === 'corn_rust') {
            ctx.fillStyle = '#b45309'; // Rust pustules
            for (let i = 0; i < 15; i++) {
                const rx = (Math.random() - 0.5) * 45;
                const ry = (Math.random() - 0.5) * 85;
                ctx.beginPath();
                ctx.arc(rx, ry, 3.5, 0, Math.PI * 2);
                ctx.fill();
            }
        } else if (type === 'grape_blackrot') {
            ctx.fillStyle = '#18181b'; // Black rot circular spots
            for (let i = 0; i < 8; i++) {
                const rx = (Math.random() - 0.5) * 50;
                const ry = (Math.random() - 0.5) * 60;
                ctx.beginPath();
                ctx.arc(rx, ry, 5, 0, Math.PI * 2);
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
        btnClear.disabled = false;

        // Automatically trigger diagnosis
        runAnalysis();
    }

    // Manual Re-Run Diagnosis
    btnAnalyze.addEventListener('click', runAnalysis);

    async function runAnalysis() {
        if (!currentImageData) return;

        // Show Laser scanner on image & update states
        scanLaser.classList.remove('hidden');
        scanningBadge.classList.remove('hidden');
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
                alert('Analysis error: ' + (data.error || 'Server error occurred'));
                loadingState.classList.add('hidden');
                emptyResults.classList.remove('hidden');
                return;
            }

            // Render all details
            renderResults(data);

        } catch (err) {
            console.error('Prediction API error:', err);
            alert('Failed to connect to the diagnosis backend server.');
            loadingState.classList.add('hidden');
            emptyResults.classList.remove('hidden');
        } finally {
            scanLaser.classList.add('hidden');
            scanningBadge.classList.add('hidden');
            btnAnalyze.disabled = false;
        }
    }

    function renderResults(data) {
        const pred = data.prediction;
        const perf = data.performance;

        // Top match header
        diseaseTitle.textContent = pred.name;
        plantCategory.textContent = `Crop: ${pred.plant} | Status: ${pred.condition}`;

        // Status & Severity Badge
        if (pred.status === 'Healthy') {
            statusPill.className = 'status-pill healthy';
            statusText.textContent = 'Healthy Leaf';
            severityPill.textContent = 'No Infection Detected';
            severityPill.style.color = 'var(--emerald)';
        } else {
            statusPill.className = 'status-pill infected';
            statusText.textContent = pred.status;
            severityPill.textContent = `${pred.severity} Severity`;
            severityPill.style.color = (pred.severity === 'Critical' || pred.severity === 'High') ? 'var(--rose)' : 'var(--amber)';
        }

        // Confidence Percentage & Bar
        confidenceNumber.textContent = `${pred.confidence_percent}%`;
        confidenceBar.style.width = `${pred.confidence_percent}%`;

        // Disease Overview Description
        diseaseDescription.textContent = pred.description || 'No detailed pathogen description available.';

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
            li.textContent = 'Leaf shows normal cellular structure with no visible pathogen symptoms.';
            symptomsList.appendChild(li);
        }

        // Treatment & Care Guide
        treatmentText.textContent = pred.treatment || 'No chemical or organic intervention required. Maintain regular watering and sunlight.';

        // Top 5 Probabilities Breakdown
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

        // Cache all classes for the 39-class explorer
        cachedAllClasses = data.all_classes || [];
        renderAllClasses(cachedAllClasses);

        // Technical Inference Performance
        specLatency.textContent = `${perf.inference_latency_ms} ms`;

        // Switch to Active View
        loadingState.classList.add('hidden');
        activeResults.classList.remove('hidden');
        lucide.createIcons();
    }

    // Render 39 Classes List
    function renderAllClasses(classes) {
        allClassesList.innerHTML = '';
        classes.forEach(c => {
            const chip = document.createElement('div');
            chip.className = 'class-chip';
            chip.innerHTML = `
                <span>${c.name}</span>
                <strong style="color: var(--cyan); margin-left: auto;">${c.probability}%</strong>
            `;
            allClassesList.appendChild(chip);
        });
    }

    // 39 Classes Toggle
    btnToggleAll.addEventListener('click', () => {
        allClassesWrapper.classList.toggle('hidden');
        const isHidden = allClassesWrapper.classList.contains('hidden');
        btnToggleAll.innerHTML = isHidden 
            ? 'Show All 39 Classes <i data-lucide="chevron-down"></i>' 
            : 'Hide Classes <i data-lucide="chevron-up"></i>';
        lucide.createIcons();
    });

    // 39 Classes Search Filter
    classSearchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const filtered = cachedAllClasses.filter(c => c.name.toLowerCase().includes(query));
        renderAllClasses(filtered);
    });

    // Print / Download Report
    btnPrintReport.addEventListener('click', () => {
        window.print();
    });
});
