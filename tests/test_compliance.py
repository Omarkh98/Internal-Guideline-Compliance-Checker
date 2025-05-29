import pytest
import ast
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import ast
import pytest
from compliance_checker import apply_compliance_rules
from config.guidelines import (
    rule_function_names_snake_case,
    rule_limit_function_length,
)

# Helper to get first function node
def get_first_function_node(code: str) -> ast.FunctionDef:
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            return node
    raise ValueError("No function found")

# === Integration tests for apply_compliance_rules ===

def test_detects_snake_case_violation():
    code = "def BadName():\n    pass"
    violations = apply_compliance_rules(code)
    for v in violations:
        print(type(v), v)
    assert any("snake_case" in v["message"] for v in violations)

def test_detects_long_function_violation():
    body = "\n".join(["    pass"] * 60)
    code = f"def long_func():\n{body}"
    violations = apply_compliance_rules(code)
    assert any(
    isinstance(v, dict) and "message" in v and "too long" in v["message"]
    for v in violations
    )

def test_function_missing_docstring():
    code = "def foo():\n    pass"
    violations = apply_compliance_rules(code)
    print("Violations:", violations)
    assert any("docstring" in v["message"].lower() for v in violations)

def test_detects_multiple_violations():
    code = "def BadFunc():\n" + "\n".join(["    pass"] * 55)
    violations = apply_compliance_rules(code)
    assert len(violations) >= 2

# === Direct unit tests for rule functions ===

def test_snake_case_rule_good_name():
    code = "def good_name():\n    pass"
    func_node = get_first_function_node(code)
    result = rule_function_names_snake_case(func_node)
    assert result == []  # expect empty list, not None

def test_snake_case_rule_bad_name():
    code = "def BadName():\n    pass"
    func_node = get_first_function_node(code)
    result = rule_function_names_snake_case(func_node)
    assert result and "snake_case" in result[0][1]

def test_function_length_rule_under_limit():
    code = "def short_func():\n    pass"
    func_node = get_first_function_node(code)
    result = rule_limit_function_length(func_node)
    assert result in (None, [])

def test_function_length_rule_over_limit():
    code = "def long_func():\n" + "\n".join(["    pass"] * 60)
    func_node = get_first_function_node(code)
    result = rule_limit_function_length(func_node)
    assert any("is too long" in message for _, message in result)