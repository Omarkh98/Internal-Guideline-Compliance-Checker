import argparse
from datetime import datetime
import json
import os
from utils import (apply_compliance_rules_with_count,
                   print_violations,
                   gather_py_files,
                   generate_markdown_report)

def main():
    parser = argparse.ArgumentParser(
        description="Check internal guideline compliance for Python file(s)."
    )
    parser.add_argument("path", type=str, help="Path to Python file or directory to check.")
    parser.add_argument("--json", "-j", action="store_true", help="Output violations as JSON")
    parser.add_argument("--summary", "-s", action="store_true", help="Output a summary only")
    parser.add_argument("--md", "-m", action="store_true", help="Output a markdown only")

    args = parser.parse_args()

    py_files = gather_py_files(args.path)  # note: args.path not args.file_path
    if not py_files:
        print(f"No Python files found at path: {args.path}")
        return

    all_violations = []
    total_functions = 0

    for file_path in py_files:
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        violations, function_count = apply_compliance_rules_with_count(code)
        for v in violations:
            v["file"] = file_path
        all_violations.extend(violations)
        total_functions += function_count

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_report_path = f"reports/report_{timestamp}"

    if args.json:
        output = json.dumps(all_violations, indent=2)  # use all_violations here
        print(output)
        with open(base_report_path + ".json", "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\nJSON report saved to {base_report_path}.json")
    elif args.summary:
        output = f"Files checked: {len(py_files)}\nFunctions checked: {total_functions}\nViolations found: {len(all_violations)}"
        print(output)
        with open(base_report_path + "_summary.txt", "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\nSummary report saved to {base_report_path}_summary.txt")
    elif args.md:
        report = generate_markdown_report(all_violations, py_files, total_functions)
        path = base_report_path + ".md"
        with open(path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\nMarkdown report saved to {path}")
    else:
        if all_violations:
            print("❌ Violations found:")
            print_violations(all_violations)
        else:
            print("✅ All checks passed. No violations found.")

if __name__ == "__main__":
    main()