#!/usr/bin/env python3
"""AI Bug Detector - starter script

Usage:
    python bug_detector.py --sector education --file path/to/file.py
"""
import ast
import argparse
import json
import os
from pathlib import Path

REPORT_PATH = Path('reports/bug_reports.json')

def load_source(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with path.open('r', encoding='utf-8') as f:
        return f.read()

def check_syntax(source):
    try:
        tree = ast.parse(source)
        return None, tree
    except SyntaxError as e:
        return {
            "lineno": e.lineno,
            "offset": e.offset,
            "msg": e.msg,
            "text": e.text.strip() if e.text else ""
        }, None

def find_docstring_issues(tree):
    issues = []
    # module docstring
    mod_doc = ast.get_docstring(tree)
    if not mod_doc:
        issues.append({
            "type": "missing_module_docstring",
            "message": "Module is missing a top-level docstring"
        })
    # functions and classes
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            doc = ast.get_docstring(node)
            if not doc:
                issues.append({
                    "type": "missing_function_docstring",
                    "name": node.name,
                    "lineno": getattr(node, 'lineno', None)
                })
        elif isinstance(node, ast.ClassDef):
            doc = ast.get_docstring(node)
            if not doc:
                issues.append({
                    "type": "missing_class_docstring",
                    "name": node.name,
                    "lineno": getattr(node, 'lineno', None)
                })
    return issues

def count_todos(source):
    return source.count('TODO') + source.count('todo') + source.count('# TODO') + source.count('#todo')

def long_function_smell(tree, source_lines, threshold=50):
    issues = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start = getattr(node, 'lineno', None)
            end = None
            # attempt to find end lineno using body
            if node.body:
                end = max(getattr(n, 'lineno', start) for n in ast.walk(node) if hasattr(n, 'lineno'))
            if start and end and (end - start) > threshold:
                issues.append({
                    "type": "long_function",
                    "name": node.name,
                    "start_lineno": start,
                    "end_lineno": end,
                    "length": end - start
                })
    return issues

def analyze_file(file_path, sector):
    source = load_source(file_path)
    syntax_err, tree = check_syntax(source)
    report = {
        "file": str(file_path),
        "sector": sector,
        "syntax_error": syntax_err,
        "issues": [],
        "metrics": {}
    }
    if syntax_err:
        return report

    doc_issues = find_docstring_issues(tree)
    todos = count_todos(source)
    lines = source.splitlines()
    lf_issues = long_function_smell(tree, lines)

    report["issues"].extend(doc_issues)
    report["issues"].extend(lf_issues)
    if todos:
        report["issues"].append({
            "type": "todos_found",
            "count": todos
        })

    report["metrics"] = {
        "lines_of_code": len(lines),
        "todo_count": todos,
        "num_issues": len(report["issues"])
    }

    return report

def save_report(report, out_path=REPORT_PATH):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # load existing
    if out_path.exists():
        try:
            with out_path.open('r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            data = []
    else:
        data = []
    data.append(report)
    with out_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Saved report to {out_path}")

def main():
    parser = argparse.ArgumentParser(description='AI Bug Detector - starter')
    parser.add_argument('--sector', required=True, choices=['education','health','environment'], help='Sector to categorize the report')
    parser.add_argument('--file', required=True, help='Path to python file to analyze')
    args = parser.parse_args()

    report = analyze_file(args.file, args.sector)
    save_report(report)

    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
