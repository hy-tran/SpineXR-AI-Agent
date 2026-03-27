# SpineXR AI Agent

Monorepo for AI engine, backend services, mobile app, and data tooling — built around the VinDr spine X-ray dataset.

## Repository structure

```
SpineXR-AI-Agent/
├── ai-engine/          # YOLO training scripts and inference service
├── backend/            # API, Supabase, security
├── mobile-app/         # Flutter frontend
├── data-tools/         # Data pipeline scripts (run once locally)
│   ├── dicom_to_jpg.py       # Step 1 – Convert DICOM → JPG
│   ├── create_yolo_labels.py # Step 2 – Convert CSV annotations → YOLO .txt
│   ├── anonymizer.py         # Strip sensitive DICOM metadata
│   └── vector_ingest.py      # Push embeddings to Pinecone
├── data/
│   ├── raw/                  # ⚠ NOT in git – download manually (see below)
│   │   ├── train_images/     # DICOM files from VinDr (~30 GB)
│   │   └── train.csv         # Original bounding-box annotations
│   └── yolo_dataset/         # ⚠ images/ and labels/ not in git – generated locally
│       ├── data.yaml         # ✅ Committed – YOLO dataset config
│       ├── images/train/
│       ├── images/val/
│       ├── labels/train/
│       └── labels/val/
└── docs/
```

## Data pipeline (run once per machine)

> Raw data is **not stored in git** (30 GB). Each team member downloads it once and runs the pipeline locally.

### 1. Download raw data

Download the VinDr-CXR dataset from Kaggle and place it under `data/raw/`:

```
data/raw/train_images/   ← DICOM files
data/raw/train.csv       ← annotation file
```

### 2. Convert DICOM → JPG

```bash
cd SpineXR-AI-Agent
python data-tools/dicom_to_jpg.py
```

Output: `data/yolo_dataset/images/`

### 3. Generate YOLO labels

```bash
python data-tools/create_yolo_labels.py
```

Output: `data/yolo_dataset/labels/`

### 4. Train the model

```bash
yolo train data=data/yolo_dataset/data.yaml model=yolov8n.pt epochs=50
```

## Setup

```bash
pip install -r ai-engine/requirements.txt
cp .env.example .env  # fill in your secrets
```
