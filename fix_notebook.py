"""
Fix SCS_main.ipynb:
- Cell 27: Fix bare newlines inside string literals + convert source to list
- Cell 37: Fix bad column names (Alert Level -> alert_level)
"""
import json
import ast
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

NOTEBOOK_PATH = r'c:\mycode\mlm_project\SCS_main.ipynb'

def load_notebook():
    with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_notebook(nb):
    with open(NOTEBOOK_PATH, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print(f"Notebook saved to {NOTEBOOK_PATH}")

def get_cell_source_str(cell):
    src = cell.get('source', [])
    if isinstance(src, list):
        return ''.join(src)
    return src

def source_to_lines(source_str):
    """Convert a source string to proper list-of-lines format."""
    lines = source_str.split('\n')
    result = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            result.append(line + '\n')
        else:
            if line:  # don't add empty last element
                result.append(line)
    return result

def has_shell_magic(source_str):
    for line in source_str.split('\n'):
        stripped = line.strip()
        if stripped.startswith('!') or stripped.startswith('%'):
            return True
    return False

def try_parse(source_str):
    try:
        ast.parse(source_str)
        return True, None
    except SyntaxError as e:
        return False, str(e)

def fix_bare_newlines_in_strings(source_str):
    """
    Fix bare newlines that appear inside string literals.

    Specifically handles patterns like:
        print('
        Results saved ...')
    Which should be:
        print('\\nResults saved ...')

    The pattern is: inside a single-quoted string, a real newline appears
    where it should be the escape \\n.

    We look for cases where a single-quote string is opened, then there's
    a literal newline, and the next line continues the string.

    Strategy: use a state machine to track whether we're inside a string.
    When we see an unescaped quote that opens a string, and then find a
    literal newline before the closing quote, replace the newline with \\n.
    """
    # We'll process character by character
    result = []
    i = 0
    n = len(source_str)

    while i < n:
        ch = source_str[i]

        # Check for triple-quoted strings first
        if source_str[i:i+3] in ('"""', "'''"):
            quote3 = source_str[i:i+3]
            result.append(quote3)
            i += 3
            # Scan until closing triple quote - don't modify content
            while i < n:
                if source_str[i:i+3] == quote3:
                    result.append(quote3)
                    i += 3
                    break
                result.append(source_str[i])
                i += 1
            continue

        # Check for single or double-quoted strings
        if ch in ('"', "'"):
            quote_char = ch
            result.append(ch)
            i += 1
            # Scan until closing quote, replacing bare newlines with \\n
            while i < n:
                c = source_str[i]
                if c == '\\' and i + 1 < n:
                    # escaped char - keep as-is
                    result.append(c)
                    result.append(source_str[i+1])
                    i += 2
                elif c == '\n':
                    # bare newline inside string - replace with \\n
                    result.append('\\n')
                    i += 1
                elif c == quote_char:
                    result.append(c)
                    i += 1
                    break
                else:
                    result.append(c)
                    i += 1
            continue

        # Check for f-strings
        if ch == 'f' and i + 1 < n and source_str[i+1] in ('"', "'"):
            result.append(ch)
            i += 1
            continue

        result.append(ch)
        i += 1

    return ''.join(result)

nb = load_notebook()
cells = nb.get('cells', [])
changes = []

print(f"Processing {len(cells)} cells...")
print()

# ---- Fix Cell 27 ----
cell27 = cells[27]
src27 = get_cell_source_str(cell27)
print(f"Cell 27 - original source type: {type(cell27.get('source')).__name__}")
print(f"Cell 27 - has bare newlines in strings: checking...")

# Check parse before fix
ok_before, err_before = try_parse(src27)
print(f"  Parse before fix: {'OK' if ok_before else f'FAIL - {err_before}'}")

# Apply fix
src27_fixed = fix_bare_newlines_in_strings(src27)
ok_after, err_after = try_parse(src27_fixed)
print(f"  Parse after fix: {'OK' if ok_after else f'FAIL - {err_after}'}")

if ok_after and not ok_before:
    # Convert to list format
    cell27['source'] = source_to_lines(src27_fixed)
    changes.append({
        'cell': 27,
        'fixes': ['Fixed bare newlines inside string literals', 'Converted source from str to list-of-lines']
    })
    print(f"  -> Fixed!")
elif ok_before:
    # Was already OK, but ensure it's a list
    if not isinstance(cell27.get('source'), list):
        cell27['source'] = source_to_lines(src27)
        changes.append({'cell': 27, 'fixes': ['Converted source from str to list-of-lines']})
        print(f"  -> Converted to list")
else:
    print(f"  -> Fix did not resolve parse error: {err_after}")
    print(f"  Fixed source preview:")
    print(src27_fixed[:500])

print()

# ---- Fix Cell 37 ----
cell37 = cells[37]
src37 = get_cell_source_str(cell37)
print(f"Cell 37 - checking column names...")

src37_fixed = src37.replace("results_df['Alert Level']", "results_df['alert_level']")
src37_fixed = src37_fixed.replace('results_df["Alert Level"]', 'results_df["alert_level"]')
src37_fixed = src37_fixed.replace("results_df['Activity Status']", "results_df['activity_status']")
src37_fixed = src37_fixed.replace('results_df["Activity Status"]', 'results_df["activity_status"]')
src37_fixed = src37_fixed.replace("results_df['Identity']", "results_df['identity']")
src37_fixed = src37_fixed.replace('results_df["Identity"]', 'results_df["identity"]')
src37_fixed = src37_fixed.replace("results_df['Confidence']", "results_df['confidence']")
src37_fixed = src37_fixed.replace('results_df["Confidence"]', 'results_df["confidence"]')
src37_fixed = src37_fixed.replace("results_df['Scene Caption']", "results_df['scene_caption']")
src37_fixed = src37_fixed.replace('results_df["Scene Caption"]', 'results_df["scene_caption"]')

if src37_fixed != src37:
    ok_after37, err_after37 = try_parse(src37_fixed)
    print(f"  Parse after fix: {'OK' if ok_after37 else f'FAIL - {err_after37}'}")
    cell37['source'] = source_to_lines(src37_fixed)
    changes.append({
        'cell': 37,
        'fixes': ["Fixed column name: 'Alert Level' -> 'alert_level' (3 occurrences)"]
    })
    print(f"  -> Fixed!")
else:
    print(f"  -> No changes needed")

print()

# ---- Also check cell 18 (source_type=str) ----
cell18 = cells[18]
if not isinstance(cell18.get('source'), list):
    src18 = get_cell_source_str(cell18)
    ok18, err18 = try_parse(src18)
    print(f"Cell 18 - source is str. Parse: {'OK' if ok18 else f'FAIL - {err18}'}")
    if ok18:
        cell18['source'] = source_to_lines(src18)
        changes.append({'cell': 18, 'fixes': ['Converted source from str to list-of-lines']})
        print(f"  -> Converted to list")
    else:
        print(f"  -> Parse error, keeping as-is")

# ---- Check cell 28 (source_type=str) ----
cell28 = cells[28]
if not isinstance(cell28.get('source'), list):
    src28 = get_cell_source_str(cell28)
    ok28, err28 = try_parse(src28)
    print(f"Cell 28 - source is str. Parse: {'OK' if ok28 else f'FAIL - {err28}'}")
    if ok28:
        cell28['source'] = source_to_lines(src28)
        changes.append({'cell': 28, 'fixes': ['Converted source from str to list-of-lines']})
        print(f"  -> Converted to list")

print()

# ---- Final verification: parse all code cells ----
print("=" * 60)
print("FINAL VERIFICATION: Parsing all code cells")
print("=" * 60)
all_pass = True
for i, cell in enumerate(cells):
    if cell.get('cell_type') != 'code':
        continue
    src = get_cell_source_str(cell)
    if has_shell_magic(src):
        print(f"  Cell {i}: SKIP (has shell magic)")
        continue
    ok, err = try_parse(src)
    if ok:
        print(f"  Cell {i}: PASS")
    else:
        print(f"  Cell {i}: FAIL - {err}")
        print(f"    Source preview: {repr(src[:200])}")
        all_pass = False

print()
print("=" * 60)
print("CHANGES SUMMARY")
print("=" * 60)
if changes:
    for change in changes:
        print(f"Cell {change['cell']}:")
        for fix in change['fixes']:
            print(f"  - {fix}")
else:
    print("No changes made.")

print()
if all_pass:
    print("All non-shell-magic code cells pass ast.parse()!")
    save_notebook(nb)
else:
    print("Some cells still fail - NOT saving. Manual review needed.")
