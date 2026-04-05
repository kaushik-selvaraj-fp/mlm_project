"""
Script to analyze and fix SCS_main.ipynb
"""
import json
import ast
import re
import sys
import io

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

NOTEBOOK_PATH = r'c:\mycode\mlm_project\SCS_main.ipynb'

def load_notebook():
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_cell_source(cell):
    """Get source as a single string."""
    src = cell.get('source', [])
    if isinstance(src, list):
        return ''.join(src)
    return src

def is_char_array(source_list):
    """Check if source is a list of individual characters (not lines)."""
    if not isinstance(source_list, list) or len(source_list) < 5:
        return False
    single_char_count = sum(1 for s in source_list if len(s) == 1)
    newline_end_count = sum(1 for s in source_list if len(s) > 1 and s.endswith('\n'))
    if single_char_count > len(source_list) * 0.5 and newline_end_count < 5:
        return True
    return False

def source_to_lines(source_str):
    """Convert a source string to proper list-of-lines format."""
    lines = source_str.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        else:
            if line:
                result.append(line)
    return result

def has_shell_magic(source_str):
    """Check if cell contains shell magic lines (starting with ! or %)."""
    lines = source_str.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('!') or stripped.startswith('%'):
            return True
    return False

def try_parse(source_str):
    """Try to parse source with ast.parse. Return (success, error)."""
    try:
        ast.parse(source_str)
        return True, None
    except SyntaxError as e:
        return False, str(e)

nb = load_notebook()
cells = nb.get('cells', [])

print(f"Total cells: {len(cells)}")
print(f"Code cells: {sum(1 for c in cells if c.get('cell_type') == 'code')}")
print()

for i, cell in enumerate(cells):
    if cell.get('cell_type') != 'code':
        continue
    src = cell.get('source', [])
    source_str = get_cell_source(cell)

    issues = []

    # Check 1: char array
    if isinstance(src, list) and is_char_array(src):
        issues.append("CHAR_ARRAY")

    # Check 5: ast.parse failures
    if not has_shell_magic(source_str):
        ok, err = try_parse(source_str)
        if not ok:
            issues.append(f"PARSE_ERROR: {err}")

    # Check 4: column name mismatches
    bad_cols = ["results_df['Alert Level']", 'results_df["Alert Level"]',
                "results_df['Activity Status']", 'results_df["Activity Status"]',
                "results_df['Identity']", 'results_df["Identity"]',
                "results_df['Confidence']", 'results_df["Confidence"]',
                "results_df['Scene Caption']", 'results_df["Scene Caption"]']
    for bc in bad_cols:
        if bc in source_str:
            issues.append(f"BAD_COLUMN: {bc}")

    if issues:
        print(f"Cell {i} (code) - ISSUES:")
        print(f"  Issues: {issues}")
        print()
    else:
        print(f"Cell {i}: OK (len={len(source_str)})")
