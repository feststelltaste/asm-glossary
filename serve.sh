#!/bin/bash
# Build both sites and serve the full output at the deployed URL structure.
# Access at: http://localhost:8000/asm-glossary/
#        DE: http://localhost:8000/asm-glossary/de/
set -e

bash "$(dirname "$0")/build.sh"

SITE_DIR="$(dirname "$0")/site"
TMP=$(mktemp -d)
SERVE_PATH="$TMP/asm-glossary"

mkdir -p "$SERVE_PATH"
cp -r "$SITE_DIR"/. "$SERVE_PATH/"

echo ""
echo "Serving at http://localhost:8000/asm-glossary/"
echo "Press Ctrl+C to stop."
python3 -m http.server 8000 --directory "$TMP"
