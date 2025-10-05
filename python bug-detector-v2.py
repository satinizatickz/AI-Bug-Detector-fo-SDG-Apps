import ast
import json
import os
import subprocess
from datetime import datetime

# -----------------------------
# AI Bug Detector v2
# -----------------------------

def analyze_with_ast(code):
    """Perform static analysis using Python AST."""
    tree = ast.parse(code)
    issues = []

    # Detect missing docstrings in functions/classes
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                issues.append({
                    "type": "Docstring",
                    "message": f"Missing docstring in {type(node).__name__}: {node.name}"
                })

    # Detect unused imports
    imports = [n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)]
    if len(imports) != len(set(imports)):
        issues.append({
            "type": "Import",
            "message": "Possible unused or duplicate imports"
        })

    # Detect long functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            start_line = node.lineno
            end_line = node.body[-1].lineno if node.body else node.lineno
            if (end_line - start_line) > 50:
                issues.append({
                    "type": "FunctionLength",
                    "message": f"Function '{node.name}' is too long ({end_line - start_line} lines)"
                })

    # Detect try/except blocks with no exception handling
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            if not node.handlers:
                issues.append({
                    "type": "ErrorHandling",
                    "message": "Try block without any except handler"
                })

    return issues


def analyze_with_pylint(filepath):
    """Run pylint and return score + messages."""
    try:
        result = subprocess.run(
            ["pylint", "--score=y", "--output-format=json", filepath],
            capture_output=True, text=True
        )
        if result.stdout:
            pylint_data = json.loads(result.stdout)
            score = None
            for line in result.stderr.split("\n"):
                if "Your code has been rated" in line:
                    score = float(line.split("/")[0].split()[-1])
            return pylint_data, score
        return [], 0.0
    except Exception as e:
        return [{"type": "PylintError", "message": str(e)}], 0.0


def detect_domain(code):
    """Simple AI domain classifier based on keyword patterns."""
    keywords = {
        "education": ["student", "teacher", "school", "classroom", "learning"],
        "health": ["patient", "hospital", "doctor", "vaccine", "disease"],
        "environment": ["climate", "tree", "pollution", "water", "recycle"]
    }

    code_lower = code.lower()
    for domain, words in keywords.items():
        if any(word in code_lower for word in words):
            return domain.capitalize()
    return "Unknown"


def generate_report(filepath):
    """Generate a full analysis report for one file."""
    with open(filepath, "r", encoding="utf-8") as f:
        code = f.read()

    ast_issues = analyze_with_ast(code)
    pylint_issues, score = analyze_with_pylint(filepath)
    domain = detect_domain(code)

    report = {
        "file": os.path.basename(filepath),
        "analyzed_on": datetime.now().isoformat(),
        "domain": domain,
        "code_quality_score": score or 0.0,
        "ast_issues": ast_issues,
        "pylint_issues": pylint_issues
    }

    os.makedirs("reports", exist_ok=True)
    out_path = os.path.join("reports", "bug_report_v2.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    print(f"✅ Analysis complete for {filepath}")
    print(f"Report saved at: {out_path}")


if __name__ == "__main__":
    print("🚀 AI Bug Detector v2 — SDG Smart Analyzer")
    target_file = input("Enter path to Python file to analyze: ").strip()

    if os.path.exists(target_file):
        generate_report(target_file)
    else:
        print("❌ File not found. Please check the path.")
