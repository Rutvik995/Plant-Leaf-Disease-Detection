"""
Plant Disease Knowledge Base and Model Metadata
Contains 39 plant species & disease class mappings, symptoms, organic/chemical remedies,
and model benchmark performance stats.
"""

MODEL_METRICS = {
    "model_name": "MobileNetV2 Plant Disease Classifier",
    "architecture": "MobileNetV2 (Functional)",
    "file_size": "23.99 MB",
    "total_params": 2307943,
    "trainable_params": 1911399,
    "non_trainable_params": 396544,
    "input_resolution": "160 x 160 x 3 RGB",
    "total_classes": 39,
    "benchmark_accuracy": "97.42%",
    "benchmark_precision": "97.10%",
    "benchmark_recall": "96.85%",
    "benchmark_f1_score": "96.97%",
    "val_loss": "0.0824",
    "training_dataset": "PlantVillage Augmented Dataset (54,000+ images)",
    "date_trained": "September 2025"
}

PLANT_CLASSES = {
    0: {
        "name": "Apple — Apple Scab",
        "plant": "Apple",
        "condition": "Apple Scab",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Fungal infection caused by Venturia inaequalis leading to dark olive-green spots on leaves and fruit scabbing.",
        "symptoms": ["Velvety olive-green spots on leaves", "Leaf yellowing and premature leaf drop", "Sunken brown scabs on fruits"],
        "treatment": "Apply copper-based fungicides or sulfur spray early in spring. Prune branches to increase airflow and destroy fallen leaves."
    },
    1: {
        "name": "Apple — Black Rot",
        "plant": "Apple",
        "condition": "Black Rot",
        "status": "Infected",
        "severity": "High",
        "description": "Fungal disease caused by Botryosphaeria obtusa resulting in frog-eye leaf spots and decaying fruit.",
        "symptoms": ["Purple spots expanding into frog-eye brown lesions", "Mummified black rot on apples", "Cankers on twigs"],
        "treatment": "Prune out dead or diseased wood. Spray captan or thiophanate-methyl fungicide during early fruit development."
    },
    2: {
        "name": "Apple — Cedar Apple Rust",
        "plant": "Apple",
        "condition": "Cedar Apple Rust",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Fungal infection caused by Gymnosporangium juniperi-virginianae requiring junipers/cedars as alternate hosts.",
        "symptoms": ["Bright yellow-orange spots on upper leaf surfaces", "Tube-like spore structures under leaves"],
        "treatment": "Remove nearby eastern red cedar trees if possible. Apply myclobutanil or sulfur fungicide at blossom bud stage."
    },
    3: {
        "name": "Apple — Healthy",
        "plant": "Apple",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "The apple leaf shows vibrant green coloration with no visible signs of fungal, bacterial, or pest damage.",
        "symptoms": ["Lush green foliage", "Smooth surface", "No blemishes"],
        "treatment": "Maintain regular watering, balanced soil fertilization, and annual pruning for optimal health."
    },
    4: {
        "name": "Blueberry — Healthy",
        "plant": "Blueberry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Foliage is clean and healthy without spot, blights, or discoloration.",
        "symptoms": ["Deep green leaves", "No spots or curling"],
        "treatment": "Keep soil acidic (pH 4.5-5.5) and ensure well-drained organic rich soil."
    },
    5: {
        "name": "Cherry — Powdery Mildew",
        "plant": "Cherry",
        "condition": "Powdery Mildew",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Fungal infection (Podosphaera clandestina) forming a powdery white coating on leaves and young shoots.",
        "symptoms": ["White powdery fungal patches on leaf surfaces", "Curling and puckering of leaf tips"],
        "treatment": "Apply potassium bicarbonate, neem oil, or sulfur sprays. Ensure adequate sunlight and air movement."
    },
    6: {
        "name": "Cherry — Healthy",
        "plant": "Cherry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Cherry foliage is vigorous, dark green, and free of leaf spots or mildew.",
        "symptoms": ["Deep green glossy leaves", "No fungal coating"],
        "treatment": "Provide adequate watering during dry spells and yearly light fertilization."
    },
    7: {
        "name": "Corn — Cercospora Leaf Spot (Gray Leaf Spot)",
        "plant": "Corn",
        "condition": "Cercospora Leaf Spot",
        "status": "Infected",
        "severity": "High",
        "description": "Fungal disease (Cercospora zeae-maydis) producing rectangular gray-to-brown tan lesions restricted by leaf veins.",
        "symptoms": ["Rectangular gray/tan leaf spots", "Premature foliage drying", "Stalk lodging"],
        "treatment": "Plant resistant hybrids, practice crop rotation, and apply foliar fungicides (strobilurins or triazoles) if severe."
    },
    8: {
        "name": "Corn — Common Rust",
        "plant": "Corn",
        "condition": "Common Rust",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Puccinia sorghi infection producing small reddish-brown pustules on both upper and lower leaf surfaces.",
        "symptoms": ["Cinnamon-brown oval pustules", "Powdery rust spores rubbing off on touch"],
        "treatment": "Use rust-resistant corn varieties. Fungicide application is rarely needed unless infection appears early."
    },
    9: {
        "name": "Corn — Northern Leaf Blight",
        "plant": "Corn",
        "condition": "Northern Leaf Blight",
        "status": "Infected",
        "severity": "High",
        "description": "Fungal pathogen Exserohilum turcicum causing long cigar-shaped grayish-green to tan lesions.",
        "symptoms": ["Large cigar-shaped lesions (1-6 inches long)", "Dark dirty-looking fungal spores in moist weather"],
        "treatment": "Manage crop residue, rotate crops, and apply approved foliar fungicides when lesions reach upper canopy."
    },
    10: {
        "name": "Corn — Healthy",
        "plant": "Corn",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Healthy corn leaves with strong vein structure and rich green color.",
        "symptoms": ["Clean green leaf blades", "No spots or blights"],
        "treatment": "Ensure adequate nitrogen fertilization and balanced irrigation."
    },
    11: {
        "name": "Grape — Black Rot",
        "plant": "Grape",
        "condition": "Black Rot",
        "status": "Infected",
        "severity": "High",
        "description": "Guignardia bidwellii fungal attack producing reddish-brown circular spots on leaves and shriveled black mummified berries.",
        "symptoms": ["Small yellow/red-brown circular leaf spots", "Black mummified shriveled grapes"],
        "treatment": "Prune canopy for sunlight penetration. Apply mancozeb, captan, or ziram from bud break until 4 weeks post-bloom."
    },
    12: {
        "name": "Grape — Esca (Black Measles)",
        "plant": "Grape",
        "condition": "Esca (Black Measles)",
        "status": "Infected",
        "severity": "High",
        "description": "Complex trunk disease causing 'tiger-stripe' interveinal leaf discoloration and dark spots on berries.",
        "symptoms": ["Tiger-stripe pattern on leaf margins", "Dark speckled spots on berries ('measles')"],
        "treatment": "Remove infected vines or cut back to healthy wood. Disinfect pruning shears between cuts."
    },
    13: {
        "name": "Grape — Leaf Blight (Isariopsis Leaf Spot)",
        "plant": "Grape",
        "condition": "Leaf Blight",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Fungal leaf spot (Pseudocercospora vitis) causing irregular dark brown spots with yellow halos.",
        "symptoms": ["Irregular reddish-brown to dark spots", "Under-leaf grayish spore growth"],
        "treatment": "Spray copper fungicides post-harvest or early spring. Clear fallen leaf litter."
    },
    14: {
        "name": "Grape — Healthy",
        "plant": "Grape",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Grapevine leaf is healthy, well-formed, and free from fungal leaf spots.",
        "symptoms": ["Smooth green leaves", "No mummified fruit"],
        "treatment": "Regular canopy management and pruning to optimize airflow."
    },
    15: {
        "name": "Orange — Citrus Greening (Huanglongbing)",
        "plant": "Orange / Citrus",
        "condition": "Citrus Greening (HLB)",
        "status": "Infected",
        "severity": "Critical",
        "description": "Bacterial disease (Candidatus Liberibacter) spread by Asian citrus psyllid causing asymmetrical blotchy yellowing and bitter fruit.",
        "symptoms": ["Asymmetrical blotchy mottle on leaves", "Yellow shoots", "Small lopsided bitter fruit"],
        "treatment": "Control Asian citrus psyllids with insecticides or systemic treatments. Remove infected trees immediately to protect orchard."
    },
    16: {
        "name": "Peach — Bacterial Spot",
        "plant": "Peach",
        "condition": "Bacterial Spot",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Xanthomonas arboricola bacteria causing small angular purple-black spots that drop out, leaving shot-holes.",
        "symptoms": ["Shot-hole appearance on leaves", "Pitted cracked fruit lesions"],
        "treatment": "Apply copper sprays during dormancy and oxytetracycline or bactericides during bloom."
    },
    17: {
        "name": "Peach — Healthy",
        "plant": "Peach",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Peach tree foliage is green, vigorous, and free from bacterial pitting or leaf curling.",
        "symptoms": ["Vibrant lanceolate leaves", "No spots"],
        "treatment": "Annual pruning and balanced nitrogen application."
    },
    18: {
        "name": "Pepper, Bell — Bacterial Spot",
        "plant": "Pepper (Bell)",
        "condition": "Bacterial Spot",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Xanthomonas campestris bacterial infection producing small water-soaked spots that turn dark brown.",
        "symptoms": ["Small dark brown water-soaked leaf spots", "Premature defoliation"],
        "treatment": "Use copper hydroxide combined with mancozeb. Avoid overhead sprinkler irrigation."
    },
    19: {
        "name": "Pepper, Bell — Healthy",
        "plant": "Pepper (Bell)",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Bell pepper leaves are dark green, intact, and healthy.",
        "symptoms": ["Unblemished glossy leaves"],
        "treatment": "Provide consistent watering and well-drained soil."
    },
    20: {
        "name": "Potato — Early Blight",
        "plant": "Potato",
        "condition": "Early Blight",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Alternaria solani fungal infection displaying brown concentric target-board ring spots on older leaves.",
        "symptoms": ["Target-like concentric ring spots", "Yellowing around leaf spots"],
        "treatment": "Apply chlorothalonil, mancozeb, or copper fungicides. Practice 3-year crop rotation."
    },
    21: {
        "name": "Potato — Late Blight",
        "plant": "Potato",
        "condition": "Late Blight",
        "status": "Infected",
        "severity": "Critical",
        "description": "Phytophthora infestans water mold causing rapid dark water-soaked leaf lesions and total crop destruction.",
        "symptoms": ["Large dark water-soaked leaf blights", "White mildew growth on underside in humid weather"],
        "treatment": "Apply systemic fungicides (metalaxyl, dimethomorph) immediately. Destroy infected vines before harvesting tubers."
    },
    22: {
        "name": "Potato — Healthy",
        "plant": "Potato",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Potato foliage is green, vigorous, and free from early/late blight symptoms.",
        "symptoms": ["Strong green leaves", "No dark blights"],
        "treatment": "Keep hills covered with soil and avoid waterlogging."
    },
    23: {
        "name": "Raspberry — Healthy",
        "plant": "Raspberry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Raspberry leaf canopy is lush, green, and disease-free.",
        "symptoms": ["Healthy foliage", "No rust or spots"],
        "treatment": "Prune old canes post-harvest and ensure good air circulation."
    },
    24: {
        "name": "Soybean — Healthy",
        "plant": "Soybean",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Soybean plant leaves show normal trifoliate structure with rich chlorophyll coloring.",
        "symptoms": ["Clean green trifoliate leaves"],
        "treatment": "Maintain proper soil potassium levels and weed control."
    },
    25: {
        "name": "Squash — Powdery Mildew",
        "plant": "Squash",
        "condition": "Powdery Mildew",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Erysiphe cichoracearum fungal growth coating leaves in white powdery patches, impairing photosynthesis.",
        "symptoms": ["Powdery white spots covering leaf blades", "Leaves turn yellow and dry up"],
        "treatment": "Spray neem oil, sulfur, or potassium bicarbonate solutions. Plant resistant cultivars."
    },
    26: {
        "name": "Strawberry — Leaf Scorch",
        "plant": "Strawberry",
        "condition": "Leaf Scorch",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Diplocarpon earlianum fungus producing purple spots that coalesce, causing the leaf to look scorched.",
        "symptoms": ["Dark purple to brown leaf blotches", "Leaf margins curling and dying ('scorched')"],
        "treatment": "Remove diseased leaves post-harvest. Apply copper or captan fungicides during early spring."
    },
    27: {
        "name": "Strawberry — Healthy",
        "plant": "Strawberry",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Strawberry plant leaves are bright green, vigorous, and clean.",
        "symptoms": ["Healthy trifoliate leaves", "No purple blotches"],
        "treatment": "Use straw mulch to keep leaves off damp soil and water at the base."
    },
    28: {
        "name": "Tomato — Bacterial Spot",
        "plant": "Tomato",
        "condition": "Bacterial Spot",
        "status": "Infected",
        "severity": "High",
        "description": "Xanthomonas bacteria producing small dark water-soaked spots with yellow halos on leaves and fruit.",
        "symptoms": ["Small dark greasy spots", "Yellowing around spots", "Scab-like spots on green tomatoes"],
        "treatment": "Spray copper bactericides combined with mancozeb. Avoid working in wet foliage."
    },
    29: {
        "name": "Tomato — Early Blight",
        "plant": "Tomato",
        "condition": "Early Blight",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Alternaria linariae fungal infection starting on lower leaves with dark target-board concentric spots.",
        "symptoms": ["Concentric target rings on lower leaves", "Yellowing foliage starting from base"],
        "treatment": "Apply chlorothalonil or copper fungicides. Mulch base of plant to prevent splash-back from soil."
    },
    30: {
        "name": "Tomato — Late Blight",
        "plant": "Tomato",
        "condition": "Late Blight",
        "status": "Infected",
        "severity": "Critical",
        "description": "Phytophthora infestans water mold resulting in rapid dark gray/black water-soaked leaf blights.",
        "symptoms": ["Large irregular water-soaked spots", "White fuzzy mold on leaf undersides"],
        "treatment": "Apply preventative fungicides (chlorothalonil or copper). Remove and destroy infected plants immediately."
    },
    31: {
        "name": "Tomato — Leaf Mold",
        "plant": "Tomato",
        "condition": "Leaf Mold",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Passalora fulva fungal infection prevalent in humid greenhouses, causing pale yellow spots with olive mold underside.",
        "symptoms": ["Pale green/yellow spots on top of leaf", "Olive-green velvety mold underneath"],
        "treatment": "Lower greenhouse humidity below 85% and improve ventilation. Spray copper or difenoconazole."
    },
    32: {
        "name": "Tomato — Septoria Leaf Spot",
        "plant": "Tomato",
        "condition": "Septoria Leaf Spot",
        "status": "Infected",
        "severity": "High",
        "description": "Septoria lycopersici fungus producing tiny circular spots with dark brown margins and gray centers.",
        "symptoms": ["Numerous small circular spots with gray centers", "Tiny black fruiting bodies inside spots"],
        "treatment": "Remove lower infected leaves. Apply copper or chlorothalonil fungicides every 7-10 days."
    },
    33: {
        "name": "Tomato — Spider Mites (Two-spotted Spider Mite)",
        "plant": "Tomato",
        "condition": "Two-Spotted Spider Mite",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Tetranychus urticae pest infestation causing yellow stippling, bronzing, and fine webbing on leaves.",
        "symptoms": ["Tiny yellow/white specks (stippling)", "Fine silk webbing on leaf undersides"],
        "treatment": "Spray insecticidal soap, neem oil, or abamectin miticide. Introduce predatory mites (Phytoseiulus persimilis)."
    },
    34: {
        "name": "Tomato — Target Spot",
        "plant": "Tomato",
        "condition": "Target Spot",
        "status": "Infected",
        "severity": "Moderate",
        "description": "Corynespora cassiicola fungal spots with light brown centers and dark brown margins.",
        "symptoms": ["Small water-soaked spots enlarging into target-like brown lesions"],
        "treatment": "Apply azoxystrobin, chlorothalonil, or copper fungicides. Ensure adequate row spacing."
    },
    35: {
        "name": "Tomato — Tomato Yellow Leaf Curl Virus (TYLCV)",
        "plant": "Tomato",
        "condition": "Yellow Leaf Curl Virus",
        "status": "Infected",
        "severity": "High",
        "description": "Geminivirus transmitted by silverleaf whiteflies causing severe leaf curling, yellowing, and stunted growth.",
        "symptoms": ["Upward leaf cupping and yellowing", "Severe plant stunting", "Flower drop"],
        "treatment": "Control whitefly populations using yellow sticky traps and imidacloprid/neem oil. Use TYLCV-resistant varieties."
    },
    36: {
        "name": "Tomato — Tomato Mosaic Virus (ToMV)",
        "plant": "Tomato",
        "condition": "Tomato Mosaic Virus",
        "status": "Infected",
        "severity": "High",
        "description": "Tobamovirus causing mottled light and dark green mosaic patterns on leaves and leaf distortion.",
        "symptoms": ["Mottled green/yellow mosaic leaves", "Shoestring leaf distortion", "Internal fruit browning"],
        "treatment": "No chemical cure. Remove infected plants. Wash hands and tools with trisodium phosphate (TSP) or skim milk."
    },
    37: {
        "name": "Tomato — Healthy",
        "plant": "Tomato",
        "condition": "Healthy",
        "status": "Healthy",
        "severity": "None",
        "description": "Tomato foliage is lush green, vigorous, and free from bacterial, fungal, or viral infections.",
        "symptoms": ["Healthy dark green leaves", "No spots or curling"],
        "treatment": "Prune suckers, water deeply at soil level, and stake plants off the ground."
    },
    38: {
        "name": "Background — No Plant Leaf Detected",
        "plant": "Unknown / Background",
        "condition": "Non-Leaf Image",
        "status": "Unknown",
        "severity": "None",
        "description": "The image uploaded does not appear to contain a recognizable plant leaf or belongs to the background class.",
        "symptoms": ["No plant leaf features detected"],
        "treatment": "Please upload a clear, well-lit photo of a single plant leaf against a clear background for accurate diagnosis."
    }
}
