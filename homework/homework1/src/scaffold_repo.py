#!/usr/bin/env python3
# Minimal scaffold helper (optional).

import pathlib, textwrap, datetime

REPO_NAME = "airbnb_price_estimator_simple"
FOLDERS = ["data/raw", "data/processed", "src", "notebooks", "docs"]
base = pathlib.Path.cwd() / REPO_NAME
base.mkdir(exist_ok=True)
for f in FOLDERS:
    (base / f).mkdir(parents=True, exist_ok=True)

README_TEMPLATE = "# See course README template — Stage 01 (keep it simple).\n"
readme_path = base / "README.md"
if not readme_path.exists():
    readme_path.write_text(README_TEMPLATE, encoding="utf-8")
print("Created:", base.resolve())
