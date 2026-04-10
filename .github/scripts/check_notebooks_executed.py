#!/usr/bin/env python3
"""Check that every code cell in every notebook has been executed."""

import json
import glob
import sys


def check_notebook(path: str) -> list[str]:
    errors = []
    with open(path) as f:
        nb = json.load(f)

    code_cells = [c for c in nb["cells"] if c["cell_type"] == "code"]
    for i, cell in enumerate(code_cells):
        source = "".join(cell["source"]).strip()
        if not source:
            continue  # skip empty code cells
        if cell.get("execution_count") is None:
            preview = source.split("\n")[0][:80]
            errors.append(f"  ⚠️  code cell {i + 1} not executed: {preview}")

    return errors


def main() -> int:
    notebooks = sorted(glob.glob("**/*.ipynb", recursive=True))
    if not notebooks:
        print("🤷 No notebooks found.")
        return 1

    failed = False
    for path in notebooks:
        errors = check_notebook(path)
        if errors:
            failed = True
            print(f"❌ {path}")
            for e in errors:
                print(e)
        else:
            print(f"✅ {path}")

    if failed:
        print("\n💥 Some notebook code cells have not been executed.")
        print("👉 Please run all cells before committing.")
        return 1

    print("\n🎉 All notebook code cells have been executed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
