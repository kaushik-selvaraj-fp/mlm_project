"""Dump specific cells for inspection."""
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

NOTEBOOK_PATH = r'c:\mycode\mlm_project\SCS_main.ipynb'

with open(NOTEBOOK_PATH, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])

# Dump cells 27 and 37 fully
for idx in [27, 37]:
    cell = cells[idx]
    src = cell.get('source', [])
    source_str = ''.join(src) if isinstance(src, list) else src
    print(f"\n{'='*60}")
    print(f"Cell {idx} (type={cell.get('cell_type')})")
    print(f"Source is list: {isinstance(src, list)}, len={len(src) if isinstance(src, list) else 'N/A'}")
    print(f"{'='*60}")
    print(source_str)
    print(f"{'='*60}")
    if isinstance(src, list):
        print("Raw list items:")
        for i, item in enumerate(src):
            print(f"  [{i}]: {repr(item)}")
