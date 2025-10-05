
🧠 AI Bug Detector for SDG Apps

An AI-powered project that automatically scans and detects bugs in Python applications supporting the UN Sustainable Development Goals (SDGs) — such as Education, Health, and Environment.

This tool helps developers ensure higher code quality and reliability for SDG-related software projects.


---

🚀 Features

Scans Python files for code quality issues

Detects syntax errors, missing docstrings, and long functions

Classifies code based on SDG domains

Generates structured bug reports in JSON format



---

🧩 AI Bug Detector v2 — SDG Smart Analyzer (New)

The AI Bug Detector v2 is the improved, smarter version of the original tool.
It introduces AI-based code understanding, Pylint integration, and domain detection to provide more meaningful insights into your code.


---

🔧 New in Version 2

✅ AST-based static analysis (finds deep code issues)

✅ Pylint integration for professional-grade scoring

✅ AI domain detection (Education, Health, Environment)

✅ Detailed JSON bug reports

✅ Organized report output under /reports/bug_report_v2.json



---

⚙️ Installation

Clone the repository:

git clone https://github.com/satinizatickz/AI-Bug-Detector-fo-SDG-Apps.git
cd AI-Bug-Detector-fo-SDG-Apps

Install dependencies for version 2:

pip install -r requirements_v2.txt


---

▶️ How to Use

Run the upgraded bug detector:

python bug_detector_v2.py

When prompted, enter the path to your .py file, for example:

sample_education.py

After running, check the generated report here:

reports/bug_report_v2.json


---

🧾 Example Output

{
    "file": "sample_education.py",
    "analyzed_on": "2025-10-05T14:23:10Z",
    "domain": "Education",
    "code_quality_score": 8.5,
    "ast_issues": [...],
    "pylint_issues": [...]
}


---

📂 Project Structure

AI-Bug-Detector-fo-SDG-Apps/
│
├── bug_detector.py            # Original basic version
├── bug_detector_v2.py         # New smart version with AI logic
├── requirements.txt
├── requirements_v2.txt
├── models/
│   ├── education_model.pkl
│   ├── health_model.pkl
│   └── environment_model.pkl
├── reports/
│   └── bug_report_v2.json
└── sample_education.py


---

🌍 Future Plans

Build Streamlit Web Dashboard (Phase 3)

Add GitHub Actions CI automation

Expand to more SDG domains (Agriculture, Energy, Water)

Integrate code fix recommendations



---

💡 Credits

Developed by Zatickz — as part of the AI for Software Engineering Project.
Empowering sustainable development through smarter software.
