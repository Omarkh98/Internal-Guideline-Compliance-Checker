import argparse
from datetime import datetime
import json
import os
from utils import (apply_compliance_rules_with_count,
                   print_violations)

def main():
    parser = argparse.ArgumentParser(
        description="Check internal guideline compliance for a Python file."
    )
    parser.add_argument("file_path", type=str, help="Path to the Python (.py) file to check.")
    parser.add_argument("--json", "-j", action="store_true", help="Output violations as JSON")
    parser.add_argument("--summary", "-s", action="store_true", help="Output a summary only")

    args = parser.parse_args()

    with open(args.file_path, "r", encoding="utf-8") as f:
        code = f.read()

    violations, function_count = apply_compliance_rules_with_count(code)

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_report_path = f"reports/report_{timestamp}"

    if args.json:
        output = json.dumps(violations, indent=2)
        print(output)
        with open(base_report_path + ".json", "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\nJSON report saved to {base_report_path}.json")
    elif args.summary:
        output = f"Functions checked: {function_count}\nViolations found: {len(violations)}"
        print(output)
        with open(base_report_path + "_summary.txt", "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\nSummary report saved to {base_report_path}_summary.txt")
    else:
        if violations:
            print("❌ Violations found:")
            print_violations(violations)
        else:
            print("✅ All checks passed. No violations found.")

if __name__ == "__main__":
    main()