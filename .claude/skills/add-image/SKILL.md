---
name: add-image
description: Add an image to a glossary term — resize, compress, copy to the right locations, and link in both EN and DE term files
argument-hint: <raw-image-filename> for <term>
allowed-tools: Read Write Edit Bash Glob Grep
---

# Add Image to Term

Workflow for processing a raw image and wiring it into the correct term files.

## Input

`$ARGUMENTS` contains a raw image filename and the term it illustrates, e.g.:
`Gemini_Generated_Image_xxx.png for sprouting`

Parse:
- **raw filename**: everything before ` for `
- **term hint**: everything after ` for `

## Workflow

### 1. Locate the raw image

Look for the file in `raw-assets/images/`. If not found, tell the user and stop.
Do not move or delete the raw image.

### 2. Locate the term files

Search `docs/` (English) and `docs/de/` (German) for a term matching the hint.
Match by filename slug or by the `# Heading` in the file.
Extract:
- `EN_FILE`: path to the English `.md` file (may not exist if hint is a German term)
- `DE_FILE`: path to the German `.md` file
- `EN_TITLE`: the `# Heading` text in the English file
- `DE_TITLE`: the `# Heading` text in the German file

**Determine intent from the hint:**
- If the hint matches an English term → this image is for both EN and DE
- If the hint matches only a German term (or is clearly a German word) → this image is German-only; only link the DE file

If no files can be found at all, tell the user and stop.

### 3. Derive the image slug

- If English term: use the English term file's basename without extension (e.g. `sprouting`)
- If German-only: use the German term file's basename without extension

This becomes the output filename: `<slug>.png`.

### 4. Process the image

**Resize to 1200px width** using Python/PIL (preserve aspect ratio; skip resize if already 1200px wide):

```bash
python3 - <<'EOF'
from PIL import Image
src = "raw-assets/images/<raw-filename>"
dst = "/tmp/<slug>.png"
img = Image.open(src)
print(f"Original: {img.width}x{img.height}")
if img.width != 1200:
    h = int(img.height * 1200 / img.width)
    img = img.resize((1200, h), Image.LANCZOS)
img.save(dst)
print(f"Output: {img.width}x{img.height}")
EOF
```

**Compress with pngquant** (in-place, overwriting the temp file):

```bash
pngquant --force --output /tmp/<slug>.png /tmp/<slug>.png
```

If pngquant fails, continue with the resized file.

### 5. Copy to destinations

Each mkdocs site has its own `docs_dir` and can only resolve paths within it. Images must be present inside each site's directory.

- **English term** (image for both EN and DE):
  ```bash
  cp /tmp/<slug>.png docs/assets/images/en/<slug>.png
  cp /tmp/<slug>.png docs/de/assets/images/<slug>.png
  ```

- **German-only term**:
  ```bash
  cp /tmp/<slug>.png docs/de/assets/images/<slug>.png
  ```

Never use `../` paths — they point outside the docs_dir and mkdocs strict mode will error.

### 6. Link in term files

Check whether each target file already contains an image tag (`![`). If it does, skip that file and tell the user.

If not present, insert the image tag between the `# Heading` and the `>` blockquote:

- **English file**: `![<EN_TITLE>](assets/images/en/<slug>.png)`
- **German file**: `![<DE_TITLE>](assets/images/<slug>.png)`

If this is a German-only image, only update the German file.

Use the Edit tool to make the insertion.

### 7. Report

Print a summary:
- Raw image: filename and original dimensions
- Output: final dimensions and file size
- Copied to: destination path(s)
- Linked in: term file path(s)
