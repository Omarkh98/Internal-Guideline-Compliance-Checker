from compliance_checker import apply_compliance_rules
import ast
import os

def print_violations(violations: list[dict]):
    seen = set()
    for v in violations:
        key = (v["id"], v["message"], v.get("line", 0))
        if key in seen:
            continue
        seen.add(key)
        line_info = f"Line {v.get('line', '?')}"
        print(f"- {v['id']} ({line_info}): {v['message']}")

def apply_compliance_rules_with_count(code: str):
    tree = ast.parse(code)
    # Count functions in the code
    function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
    violations = apply_compliance_rules(code)
    return violations, function_count


def gather_py_files(path: str) -> list[str]:
    if os.path.isfile(path) and path.endswith(".py"):
        return [path]
    elif os.path.isdir(path):
        py_files = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
        return py_files
    else:
        return []
    
def generate_markdown_report(violations: list[dict], py_files, total_functions: int) -> str:
    md = f"# Internal Guidelines Compliance Report\n\n"
    md += f"**Files checked:** {len(py_files)}\n\n"
    md += f"**Functions checked:** {total_functions}\n\n"
    md += f"**Violations found:** {len(violations)}\n\n"
    
    if not violations:
        md += "✅ All checks passed. No violations found.\n"
        return md

    md += "| File | Line | Violation |\n"
    md += "|------|------|-----------|\n"
    for v in violations:
        md += f"| {v.get('file', 'N/A')} | {v['line']} | {v['message']} |\n"
    return md