#!/usr/bin/env python3
"""
Generate glossary term images using the Gemini Flash image generation API.

For each term file that lacks an image, this script:
  1. Reads the term title and description from the markdown front matter / body.
  2. Sends a generation prompt to Gemini Flash.
  3. Saves the raw PNG to raw-assets/images/.
  4. Resizes to 1200 px width and compresses with pngquant.
  5. Copies the result to docs/assets/images/en/<slug>.png
     and docs/de/assets/images/<de-slug>.png.
  6. Injects the image reference into both the English and German term files
     (if not already present).

Usage:
    export GEMINI_API_KEY="your-key"
    python scripts/generate_images.py [--term context-rot] [--dry-run]

Dependencies:
    pip install google-genai pillow
    pngquant must be on PATH
"""

import argparse
import base64
import os
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path

# ---------------------------------------------------------------------------
# Optional: install google-genai on the fly if missing
# ---------------------------------------------------------------------------
try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Installing google-genai …")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])
    from google import genai
    from google.genai import types

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow …")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

import io

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent
DOCS_EN = REPO_ROOT / "docs"
DOCS_DE = REPO_ROOT / "docs" / "de"
RAW_ASSETS = REPO_ROOT / "raw-assets" / "images"
EN_IMG_DIR = DOCS_EN / "assets" / "images" / "en"
DE_IMG_DIR = DOCS_DE / "assets" / "images"

MODELS = {
    "nano-banana-2": "gemini-3.1-flash-image-preview",
    "nano-banana-pro": "gemini-3-pro-image-preview",
}
DEFAULT_MODEL = "nano-banana-2"
TARGET_WIDTH = 1200


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict:
    """Return key→value dict from YAML front matter (simple key: value only)."""
    fm = {}
    if not text.startswith("---"):
        return fm
    end = text.find("---", 3)
    if end == -1:
        return fm
    for line in text[3:end].splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm


def extract_blockquote(text: str) -> str:
    """Return the first blockquote (> …) stripped of the leading >."""
    lines = []
    in_quote = False
    for line in text.splitlines():
        if line.startswith(">"):
            lines.append(line[1:].strip())
            in_quote = True
        elif in_quote:
            break
    return " ".join(lines)


def slug_from_file(path: Path) -> str:
    return path.stem


def image_already_linked(text: str, slug: str) -> bool:
    return f"![" in text and slug in text


def inject_image_into_md(md_path: Path, img_rel_path: str, slug: str) -> None:
    """Insert an image reference after the first heading in the markdown file."""
    text = md_path.read_text(encoding="utf-8")
    if image_already_linked(text, slug):
        return
    # Find first H1 line
    lines = text.splitlines(keepends=True)
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            insert_at = i + 1
            break
    if insert_at is None:
        return
    img_line = f"\n![{slug}]({img_rel_path})\n"
    lines.insert(insert_at, img_line)
    md_path.write_text("".join(lines), encoding="utf-8")
    print(f"  Injected image reference into {md_path.relative_to(REPO_ROOT)}")


def resize_to_width(img_bytes: bytes, width: int) -> bytes:
    """Resize image bytes to the given width, preserving aspect ratio."""
    img = Image.open(io.BytesIO(img_bytes))
    if img.width != width:
        ratio = width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((width, new_height), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def run_pngquant(png_path: Path) -> None:
    """Compress a PNG in-place with pngquant."""
    if shutil.which("pngquant") is None:
        print("  WARNING: pngquant not found on PATH — skipping compression")
        return
    result = subprocess.run(
        ["pngquant", "--force", "--output", str(png_path), str(png_path)],
        capture_output=True,
    )
    if result.returncode not in (0, 98):  # 98 = already optimal
        print(f"  WARNING: pngquant exited with {result.returncode}: {result.stderr.decode()}")


def build_prompt(title: str, description: str) -> str:
    return (
        "Create an image as a clean, minimalist black and white line art illustration. "
        "Style: Modern vector-style textbook diagram. Solid black outlines on a pure white background. "
        "No shading, no textures, no text, no titles. High contrast, isolated on white. "
        "Keep the illustration extremely minimalistic: use as few lines and shapes as possible "
        "to convey the concept. Avoid decorative elements, unnecessary details, and visual clutter. "
        f"Professional and clinical. Topic: {title} — {description}"
    )


# ---------------------------------------------------------------------------
# Main generation logic
# ---------------------------------------------------------------------------

def collect_term_files(term_filter: str | None) -> list[Path]:
    """Return all English term .md files (excluding index/about/concept-maps)."""
    excluded = {"index.md", "about.md", "concept-maps.md"}
    files = []
    for md in sorted(DOCS_EN.rglob("*.md")):
        if md.name in excluded:
            continue
        if "de/" in str(md.relative_to(REPO_ROOT)):
            continue
        if term_filter and md.stem != term_filter:
            continue
        files.append(md)
    return files


def find_de_file(fm: dict) -> Path | None:
    """Locate the German counterpart using front matter translation_de key."""
    de_slug = fm.get("translation_de")
    if not de_slug:
        return None
    matches = list(DOCS_DE.rglob(f"{de_slug}.md"))
    return matches[0] if matches else None


def generate_image(client: genai.Client, prompt: str, model: str, dry_run: bool) -> bytes | None:
    if dry_run:
        print(f"  [dry-run] Would call {model}")
        return None

    response = client.models.generate_content(
        model=model,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    for part in response.parts:
        if part.inline_data is not None:
            return part.inline_data.data

    print("  WARNING: no image returned by the API")
    return None


def process_term(md_path: Path, client: genai.Client, model: str, variations: int, dry_run: bool) -> None:
    text = md_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    title = fm.get("title") or md_path.stem.replace("-", " ").title()
    description = extract_blockquote(text) or f"A concept in agentic software modernization: {title}"
    en_slug = slug_from_file(md_path)

    en_img_dest = EN_IMG_DIR / f"{en_slug}.png"

    if en_img_dest.exists():
        print(f"  Skipping {en_slug} (image already exists)")
        return

    print(f"\n→ {en_slug}")
    print(f"  Title:  {title}")
    print(f"  Model:  {model}")
    print(f"  Variations: {variations}")
    print(f"  Prompt: {description[:80]}…")

    RAW_ASSETS.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(title, description)

    # --- Generate variations ---
    results: list[bytes] = []
    for i in range(1, variations + 1):
        if variations > 1:
            print(f"  Generating variation {i}/{variations} …")
        img_bytes = generate_image(client, prompt, model, dry_run)
        if dry_run:
            return
        if img_bytes is None:
            continue
        suffix = f"-{i}" if variations > 1 else ""
        raw_path = RAW_ASSETS / f"{en_slug}{suffix}.png"
        raw_path.write_bytes(img_bytes)
        results.append(img_bytes)
        if variations > 1:
            print(f"  Saved raw variation → {raw_path.relative_to(REPO_ROOT)}")

    if not results:
        return

    if variations > 1:
        print(f"\n  {variations} variations saved to {RAW_ASSETS.relative_to(REPO_ROOT)}/")
        print(f"  Files: {', '.join(f'{en_slug}-{i}.png' for i in range(1, len(results) + 1))}")
        print(f"  Using variation 1 — delete the others you don't want from raw-assets/images/")
    img_bytes = results[0]

    # --- Resize to 1200 px ---
    resized = resize_to_width(img_bytes, TARGET_WIDTH)

    # --- Save to EN docs and run pngquant ---
    EN_IMG_DIR.mkdir(parents=True, exist_ok=True)
    en_img_dest.write_bytes(resized)
    run_pngquant(en_img_dest)
    print(f"  Saved  {en_img_dest.relative_to(REPO_ROOT)}")

    # --- Inject into English term file ---
    inject_image_into_md(md_path, f"assets/images/en/{en_slug}.png", en_slug)

    # --- German counterpart ---
    de_md = find_de_file(fm)
    if de_md:
        de_slug = slug_from_file(de_md)
        DE_IMG_DIR.mkdir(parents=True, exist_ok=True)
        de_img_dest = DE_IMG_DIR / f"{de_slug}.png"
        shutil.copy2(en_img_dest, de_img_dest)
        print(f"  Copied {de_img_dest.relative_to(REPO_ROOT)}")
        inject_image_into_md(de_md, f"assets/images/{de_slug}.png", de_slug)
    else:
        print(f"  WARNING: no German counterpart found for {en_slug}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate glossary images with Gemini Flash")
    parser.add_argument("--term", help="Process only this term slug (e.g. context-rot)")
    parser.add_argument(
        "--next",
        type=int,
        metavar="N",
        help="Process only the next N terms that have no image yet",
    )
    parser.add_argument("--dry-run", action="store_true", help="Parse terms but skip API calls")
    parser.add_argument(
        "--model",
        choices=list(MODELS.keys()),
        default=DEFAULT_MODEL,
        help="Image model to use (default: nano-banana-2)",
    )
    parser.add_argument(
        "--variations",
        type=int,
        default=1,
        metavar="N",
        help="Number of image variations to generate per term (you pick the best one)",
    )
    args = parser.parse_args()
    model = MODELS[args.model]

    if args.variations < 1:
        sys.exit("ERROR: --variations must be at least 1.")
    if args.next is not None and args.next < 1:
        sys.exit("ERROR: --next must be at least 1.")

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and not args.dry_run:
        sys.exit("ERROR: GEMINI_API_KEY environment variable is not set.")

    client = genai.Client(api_key=api_key) if api_key else None

    term_files = collect_term_files(args.term)
    if not term_files:
        sys.exit(f"No term files found{f' for slug {args.term!r}' if args.term else ''}.")

    if args.next is not None:
        term_files = [
            f for f in term_files
            if not (EN_IMG_DIR / f"{f.stem}.png").exists()
        ][:args.next]

    print(f"Found {len(term_files)} term(s) to process.")

    for md_path in term_files:
        process_term(md_path, client, model, args.variations, args.dry_run)

    print("\nDone.")


if __name__ == "__main__":
    main()
