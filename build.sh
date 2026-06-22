#!/bin/bash
set -e

echo "Updating nav and index..."
python scripts/update_overview.py

echo "Building English site..."
mkdocs build --strict

echo "Building German site..."
mkdocs build --strict -f mkdocs-de.yml

echo "Copying self-assessment..."
cp -r self-assessment/ site/self-assessment/

echo "Done. Site output in site/"
