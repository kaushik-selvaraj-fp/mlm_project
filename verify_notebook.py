"""Quick verification of fixed cells."""
import json
import ast
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

NOTEBOOK_PATH = r'c:\mycode\mlm_project\SCS_main.ipynb'

with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])

# Spot-check cells 18, 27, 28, 37
for idx in [18, 27, 28, 37]:
    cell = cells[idx]
    src = cell.get('source', [])
    source_str = ''.join(src) if isinstance(src, list) else src
    src_type = type(src).__name__

    print(f"\nCell {idx} (source type={src_type}):")
    print(f"  First 200 chars: {repr(source_str[:200])}")

    # Parse check
    try:
        ast.parse(source_str)
        print(f"  ast.parse: OK")
    except SyntaxError as e:
        print(f"  ast.parse: FAIL - {e}")

print("\n\nAll code cells parse check:")
for i, cell in enumerate(cells):
    if cell.get('cell_type') != 'code':
        continue
    src = cell.get('source', [])
    source_str = ''.join(src) if isinstance(src, list) else src
    # Skip shell magic
    has_magic = any(l.strip().startswith(('!', '%')) for l in source_str.split('\n'))
    if has_magic:
        print(f"  Cell {i}: SKIPPED (shell magic)")
        continue
    try:
        ast.parse(source_str)
        print(f"  Cell {i}: PASS")
    except SyntaxError as e:
        print(f"  Cell {i}: FAIL - {e}")
