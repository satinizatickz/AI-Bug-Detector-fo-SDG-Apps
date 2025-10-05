# AI Bug Detector for SDG Apps

A starter project that scans Python source files for basic issues and generates a sector-specific bug report.
Sectors supported: `education`, `health`, `environment`.

## Quick start

1. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the detector:
```bash
python bug_detector.py --sector education --file path/to/your_script.py
```

3. Reports are saved to `reports/bug_reports.json`.

## What this starter detects
- Syntax errors
- Missing module/class/function docstrings
- `TODO` markers
- Long functions (> 50 lines) as a simple code-smell heuristic

## Project structure
```
AI-Bug-Detector-for-SDG-Apps/
├── bug_detector.py
├── requirements.txt
├── README.md
├── data/
│   ├── education/
│   ├── health/
│   └── environment/
├── models/
│   ├── education_model.pkl
│   ├── health_model.pkl
│   └── environment_model.pkl
└── reports/
    └── bug_reports.json
```

You can extend this project by adding NLP/ML models per sector, integrating static analysis tools, or building a web UI with Streamlit.
