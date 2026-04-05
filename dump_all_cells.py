"""Dump all code cells for inspection."""
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

NOTEBOOK_PATH = r'c:\mycode\mlm_project\SCS_main.ipynb'

with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])

for idx, cell in enumerate(cells):
    if cell.get('cell_type') != 'code':
        continue
    src = cell.get('source', [])
    source_str = ''.join(src) if isinstance(src, list) else src
    print(f"\n{'='*60}")
    print(f"Cell {idx} (type=code, source_type={type(src).__name__})")
    print(f"{'='*60}")
    print(source_str)
