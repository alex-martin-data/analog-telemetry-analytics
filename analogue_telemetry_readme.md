# Analogue Telemetry & DSP Analytics Platform

An enterprise-grade, Hardware-in-the-Loop (HIL) telemetry ingestion and Digital Signal Processing (DSP) analytics platform. This system captures analogue circuit signals, extracts time- and frequency-domain audio metrics in Python, loads structured telemetry into Google BigQuery, and models analytical data marts using dbt Core.

## 🏛 Platform Architecture

```
                               ┌───────────────────────────────────────────────────────────┐
                               │                    PYTHON DSP PIPELINE                    │
                               │                                                           │
┌──────────────────────┐       │  ┌─────────────────┐   ┌───────────────────────────────┐  │       ┌──────────────────────┐       ┌──────────────────────┐
│  Hardware Test Bench │  WAV  │  │  librosa / scipy│   │  Feature Extraction           │  │ PARQUET│    Google BigQuery   │  dbt  │   dbt Analytics      │
│  (Analogue Signals)  ├───────┼─►│  Signal Ingestion──┼──►  - THD (Total Harmonic Dist.) ├──┼──────►│   (Bronze / Raw Layer)├──────►│   Data Marts         │
│                      │       │  │                 │   │  - Spectral Centroid / Rolloff│  │        │                      │       │   (Gold Layer)       │
└──────────────────────┘       │  └─────────────────┘   │  - RMS Energy & Peak dB       │  │        └──────────────────────┘       └──────────────────────┘
                               │                        └───────────────────────────────┘  │
                               └───────────────────────────────────────────────────────────┘

```

The data pipeline processes analogue audio circuit telemetry through four core stages:

1. **Analogue Ingestion & DSP Feature Extraction (Python):** Reads raw `.wav` recordings from hardware test runs, computes Digital Signal Processing (DSP) features (Total Harmonic Distortion, spectral metrics, peak RMS amplitudes), and structures metrics using `Polars`.

2. **Staging & Storage:** Converts processed telemetry into columnar Parquet files for fast, low-cost upload to Google BigQuery storage.

3. **Data Warehousing (BigQuery):** Houses bronze staging tables and partitioned telemetry data structures.

4. **Data Transformation & Analytics (dbt Core):** Transforms raw telemetry into analytical data marts (silver/gold), executing automated quality checks, testing harmonic tolerances, and materialising performance metrics.

## 📁 Repository Structure

```
analog-telemetry-analytics/
├── .vscode/                        # Editor settings (enforcing en-GB spellcheck)
├── data/
│   ├── raw/                        # Ingested .wav hardware recordings
│   └── processed/                  # Processed Parquet data exports
├── python/
│   ├── dsp/                        # Digital Signal Processing modules
│   │   └── generate_dummy_audio.py # Test signal synthesis script
│   └── bigquery/                   # Ingestion scripts for GCP BigQuery
├── dbt/
│   └── telemetry_analytics/        # dbt Core transformation project
│       ├── models/
│       │   ├── staging/            # Staging views & signal sanitisation
│       │   └── marts/              # Analytics tables & performance marts
│       └── dbt_project.yml         # dbt project configuration
├── .gitignore                      # Git exclusion rules
└── README.md                       # Platform documentation

```

## ⚙️ Tech Stack & Dependencies

* **Language & Runtime:** Python 3.11+

* **Signal Processing & Data Processing:** `librosa`, `scipy`, `numpy`, `polars`

* **Data Warehousing & Modelling:** Google BigQuery, `dbt-core`, `dbt-bigquery`

* **Version Control & Tooling:** Git, GitHub CLI (`gh`), macOS (Apple Silicon M2)

## 🚀 Quick Start Guide

### 1. Prerequisites & Environment Setup

Clone the repository and initialise the Python virtual environment:

```
git clone https://github.com/alex-martin-data/analog-telemetry-analytics.git
cd analog-telemetry-analytics

# Create and activate local virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install pipeline dependencies
pip install --upgrade pip
pip install polars librosa scipy google-cloud-bigquery dbt-bigquery

```

### 2. Generate Synthetic Test Telemetry

Generate baseline sine-wave signals matching the 4-test bench matrix prior to hardware ingestion:

```
python python/dsp/generate_dummy_audio.py

```

Verify output audio files inside the raw data directory:

```
ls -la data/raw

```

### 3. Compile dbt Models

Navigate to the dbt project directory to compile transformation models:

```
cd dbt/telemetry_analytics
dbt compile

```

## 📜 Engineering Standards & Conventions

* **Language Standard:** British English (`en-GB`) enforced across all SQL models, Python docstrings, dbt documentation, and Git commit history.

* **Commit Style:** Conventional Commits standard (`feat:`, `fix:`, `chore:`, `docs:`).

* **Environment Boundaries:** Strict isolation between client IP and portfolio repositories using local Git configuration (`git config --local`).

## 📄 License

Distributed under the MIT License.