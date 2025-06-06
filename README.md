# Internal Guideline Compliance Checker

A multi-language tool to analyze source code files for internal coding guideline violations, helping teams maintain consistent, clean, and compliant codebases.

---

## Features

- Checks source code files in **Python**, **Java**, and **XML**.
- Recursively scans directories for supported files.
- Applies node-level and tree-level compliance rules tailored for each language.
- Supports multiple output formats:
  - Detailed JSON reports
  - Summary reports
  - Markdown reports (human-readable, shareable)
- Generates timestamped reports saved in a `reports/` folder.
- Easily integrates with CI/CD pipelines or LLM-based tool orchestrators.
- CLI-invokable and Python-callable for flexible automation.



## Supported Languages & Rules

| Language | File Extensions | Key Compliance Checks                                |
|----------|-----------------|-----------------------------------------------------|
| Python   | `.py`           | Syntax errors, naming conventions, docstrings, function length, code style |
| Java     | `.java`         | Package declarations, Javadoc presence, method length, logger usage, wildcard imports |
| XML      | `.xml`          | Well-formedness, project metadata (name, description, url), tag and attribute conventions |



## Usage
Run the checker from the command line:
```bash
python main.py <path> [options]
```
Where `<path>` is a path to a Python file or a directory containing Python files.

### Command Line Options
1. **--json**, **-j**:  Output violations as a detailed JSON report. Saved in `reports/`.

2. **--summary**, **-s**: Output a concise summary of the checks and violations. Saved in `reports/`.

3. **--md**, **-m**: Output a Markdown formatted report. Saved in `reports/`.

## Examples
1.	Check a single Python, Java, or XML file and print violations to the console:

```bash
python main.py path/to/file.py
python main.py path/to/file.java
python main.py path/to/file.xml
```
2. Check a whole directory recursively and get a JSON report:

```bash
python main.py path/to/project --json
```
3. Generate a summary report for a directory:

```bash
python main.py path/to/project --summary
```

4. Generate a Markdown report:
```bash
python main.py path/to/project --md
```

## LLM Callable Function:
`check_compliance`

```bash
from main import check_compliance

violations, function_count = check_compliance("path/to/file_or_folder.py")

for v in violations:
    print(v)
```

## Project Metadata
Tool metadata available in `tool_metadata.json`

## Testing
Run all tests:
```bash
pip install pytest

pytest tests/
```

## Output Structure
```
reports/
├── report_20250530_142312.json
├── report_20250530_142312_summary.txt
├── report_20250530_142312.md
```