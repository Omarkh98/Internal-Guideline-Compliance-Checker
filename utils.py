from compliance_checker import apply_compliance_rules
import ast

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