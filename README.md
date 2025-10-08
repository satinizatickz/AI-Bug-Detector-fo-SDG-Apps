


--

# 🐞 AI Bug Detector for SDG Apps

> **AI Bug Detector for SDG Apps** is an intelligent Python-based tool that automatically detects bugs, code smells, and quality issues in software projects aligned with the **United Nations Sustainable Development Goals (SDGs)** — such as education, health, and environment applications.

---

## 🎯 Project Objectives

1. **Support SDG Innovation** — Encourage developers building impactful SDG solutions by helping them detect and fix bugs early.  
2. **Improve Code Quality** — Promote clean, maintainable, and reliable software in AI-driven SDG applications.  
3. **Automate Bug Detection** — Provide a lightweight AI-assisted static analysis tool for Python developers.  
4. **Bridge AI and Sustainability** — Demonstrate how artificial intelligence can improve sustainable development software practices.

---

## 💡 Core Values

- 🌍 **Sustainability** — Every line of code should serve global good.  
- 🤖 **Innovation** — Using AI to detect, prevent, and improve.  
- 🔍 **Transparency** — Clear, interpretable bug reports for learning.  
- 💪 **Empowerment** — Helping developers build error-free SDG apps faster.  
- 📈 **Growth** — Continuous improvement through feedback and collaboration.

---

## 🚀 Key Features

- Detects **syntax errors** and structural problems.  
- Flags **missing docstrings** in functions and classes.  
- Identifies **TODO/FIXME** comments to track incomplete work.  
- Detects **long functions** (> 50 lines) as code smell indicators.  
- Generates structured **JSON reports** for easy review.  
- Sector-aware analysis for **Education**, **Health**, and **Environment** projects.

---

## 🧩 Supported SDG Sectors

| Sector | Description |
|--------|--------------|
| **Education** | Checks for clarity and maintainability in learning-focused apps. |
| **Health** | Ensures reliability and safety in health-related Python code. |
| **Environment** | Detects inefficiencies and potential issues in environmental monitoring apps. |

--


---

🧠 Usage Example

Run the bug detector on a Python file of your choice:

python bug_detector.py --sector education --file path/to/your_script.py

Example Output:

{
  "file": "example.py",
  "sector": "education",
  "issues_detected": 3,
  "issues": [
    "Function 'train_model' is missing a docstring.",
    "Line 42: Found TODO comment.",
    "Function 'process_data' is too long (72 lines)."
  ]
}

Reports are saved in the reports/bug_reports.json file.


---

📊 Folder Structure

AI-Bug-Detector-for-SDG-Apps/
│
├── bug_detector.py        # Main analysis logic
├── data/                  # Sample or input files
├── reports/               # JSON output reports
├── tests/                 # Unit tests for bug detector
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── LICENSE                # Open-source license


---

🧰 Technologies Used

Python 3.9+

AST (Abstract Syntax Tree)

JSON for structured reports

Logging for professional tracking

Argparse for command-line interface



---

🧪 Testing

Run automated tests using:

pytest tests/


---

🧭 Future Roadmap

[ ] Add a Streamlit dashboard for live visual bug reports

[ ] Integrate with GitHub Actions for automatic code scanning

[ ] Include Bandit / Flake8 for advanced static analysis

[ ] Add machine learning bug prediction models

[ ] Extend support to JavaScript, Java, and other SDG-related languages



---

🧾 License

MIT License

MIT License

Copyright (c) 2025 Satini Zatickz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---

👨‍💻 Author Information

Name: Satini Zatickz
Role: Software Developer | AI Engineer | Digital Innovator
Email: satinizatickz@gmail.com
GitHub: github.com/satinizatickz
Project Link: AI Bug Detector for SDG Apps


---

💬 Acknowledgments

Inspired by the UN Sustainable Development Goals (SDGs) framework.

Supported by the Power Learn Project (PLP) - AI for Software Engineering initiative.

Built to promote clean, sustainable, and intelligent coding practices.



---

🏆 Vision

To empower African youth and global developers to build smart, sustainable, and bug-free software that contributes to achieving the United Nations Sustainable Development Goals through AI-powered software Engineering 


