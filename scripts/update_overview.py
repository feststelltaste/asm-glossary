#!/usr/bin/env python3
"""
Generate mkdocs.yml and mkdocs-de.yml nav from flat docs/ file structure,
then regenerate the Categories table in docs/index.md and docs/de/index.md.

Term files live flat in docs/<term>.md with front matter:
  ---
  title: Agent Memory
  category: 🤖 Grundlagen
  ---

Workflow for adding a new term:
  1. Create docs/<term>.md (with title + category front matter)
  2. Create docs/de/<term>.md (with title + category front matter)
  3. Run:  python scripts/update_overview.py
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml  (included with mkdocs-material)")

REPO_ROOT = Path(__file__).resolve().parent.parent
MKDOCS_YML = REPO_ROOT / "mkdocs.yml"
MKDOCS_DE_YML = REPO_ROOT / "mkdocs-de.yml"
DOCS_DIR = REPO_ROOT / "docs"
DOCS_DE_DIR = DOCS_DIR / "de"
INDEX_MD = DOCS_DIR / "index.md"
INDEX_DE_MD = DOCS_DE_DIR / "index.md"
CONCEPT_MAPS_MD = DOCS_DIR / "concept-maps.md"

# Non-term files to ignore when scanning flat docs/
NON_TERM_FILES = {"index.md", "about.md", "concept-maps.md"}

# Home is in nav for sidebar context; About/Concept Maps are in header buttons
STATIC_NAV_ITEMS_EN = [{"Home": "index.md"}]
STATIC_NAV_ITEMS_DE = [{"Startseite": "index.md"}]

# Canonical category order (English labels); unknown categories are appended alphabetically
CATEGORY_ORDER = [
    "Grundlagen",
    "Infrastruktur",
    "Analysis & Knowledge",
    "Modernization",
    "Testing & Verification",
    "Engineering & Control",
]

# Map English category label → category dir (for index.md links in nav)
CATEGORY_DIR = {
    "Grundlagen": "agent-fundamentals",
    "Infrastruktur": "agent-infrastructure",
    "Analysis & Knowledge": "analysis-knowledge",
    "Modernization": "modernization",
    "Testing & Verification": "testing-verification",
    "Engineering & Control": "engineering-control",
}

# Map English category label → German category label
CATEGORY_LABEL_DE = {
    "Grundlagen": "Grundlagen",
    "Infrastruktur": "Infrastruktur",
    "Analysis & Knowledge": "Analyse & Wissen",
    "Modernization": "Modernisierung",
    "Testing & Verification": "Testing & Absicherung",
    "Engineering & Control": "Entwicklung & Kontrolle",
}

# Map German category label → category dir
CATEGORY_DIR_DE = {v: k_dir for (k, v), k_dir in
                   zip(CATEGORY_LABEL_DE.items(), CATEGORY_DIR.values())}


def parse_front_matter(content: str) -> dict:
    """Extract YAML front matter from a markdown file. Returns {} if none."""
    m = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def get_h1(path: Path) -> str:
    """Return the first H1 heading from a markdown file."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def scan_categories_flat(docs_dir: Path, category_order: list[str]) -> list[dict]:
    """
    Scan flat docs_dir for term files (those with 'category' front matter).
    Returns a list of nav dicts ordered by category_order.
    Each dict: { "Category Label": ["cat-dir/index.md", {"Term": "term.md"}, ...] }
    """
    term_files = sorted(
        f for f in docs_dir.iterdir()
        if f.suffix == ".md" and f.name not in NON_TERM_FILES and f.is_file()
    )

    # Group by category
    categories: dict[str, list[tuple[str, str]]] = {}
    for tf in term_files:
        content = tf.read_text(encoding="utf-8")
        meta = parse_front_matter(content)
        if "category" not in meta:
            continue
        cat = meta["category"]
        title = meta.get("title") or get_h1(tf)
        categories.setdefault(cat, []).append((title, tf.name))

    # Sort terms within each category
    for cat in categories:
        categories[cat].sort(key=lambda x: x[0])

    # Build ordered nav list
    known = [c for c in category_order if c in categories]
    unknown = sorted(c for c in categories if c not in category_order)

    nav_categories = []
    for cat in known + unknown:
        # Determine index.md path
        cat_dir = CATEGORY_DIR.get(cat) or CATEGORY_DIR_DE.get(cat)
        entries = []
        if cat_dir and (docs_dir / cat_dir / "index.md").exists():
            entries.append(f"{cat_dir}/index.md")
        for title, filename in categories[cat]:
            entries.append({title: filename})
        nav_categories.append({cat: entries})

    return nav_categories


def replace_nav_in_yml(yml_path: Path, nav_categories: list[dict]) -> None:
    """Replace the nav: block in a mkdocs yml file."""
    nav_yaml = yaml.dump(
        {"nav": nav_categories},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        indent=2,
    )

    original = yml_path.read_text(encoding="utf-8")
    updated = re.sub(
        r"^nav:.*?(?=^\w|\Z)",
        nav_yaml + "\n",
        original,
        flags=re.MULTILINE | re.DOTALL,
    )

    rel = yml_path.relative_to(REPO_ROOT)
    if updated != original:
        yml_path.write_text(updated, encoding="utf-8")
        print(f"Updated nav in {rel}")
    else:
        print(f"{rel}: no changes")


def update_mkdocs_nav(nav_categories: list[dict]) -> list[dict]:
    full_nav = STATIC_NAV_ITEMS_EN + nav_categories
    replace_nav_in_yml(MKDOCS_YML, full_nav)
    return full_nav


def update_mkdocs_de_nav(nav_categories_en: list[dict]) -> None:
    """Build German nav from the German docs dir and update mkdocs-de.yml."""
    # Derive German category order from English order
    de_order = [CATEGORY_LABEL_DE.get(c, c) for c in CATEGORY_ORDER]
    nav_de = STATIC_NAV_ITEMS_DE + scan_categories_flat(DOCS_DE_DIR, de_order)

    # mkdocs-de.yml may have no nav section yet — add one if missing
    original = MKDOCS_DE_YML.read_text(encoding="utf-8")
    nav_yaml = yaml.dump(
        {"nav": nav_de},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        indent=2,
    )

    if re.search(r"^nav:", original, re.MULTILINE):
        updated = re.sub(
            r"^nav:.*?(?=^\w|\Z)",
            nav_yaml + "\n",
            original,
            flags=re.MULTILINE | re.DOTALL,
        )
    else:
        # Append nav before the first top-level key after plugins/markdown_extensions
        updated = original.rstrip() + "\n\n" + nav_yaml

    if updated != original:
        MKDOCS_DE_YML.write_text(updated, encoding="utf-8")
        print("Updated nav in mkdocs-de.yml")
    else:
        print("mkdocs-de.yml: no changes")


def update_index(docs_dir: Path, index_path: Path, category_order: list[str]) -> None:
    """Regenerate category sections in an index.md from flat term files."""
    if not index_path.exists():
        print(f"{index_path.relative_to(REPO_ROOT)}: not found, skipping")
        return

    term_files = sorted(
        f for f in docs_dir.iterdir()
        if f.suffix == ".md" and f.name not in NON_TERM_FILES and f.is_file()
    )

    categories: dict[str, list[tuple[str, str]]] = {}
    for tf in term_files:
        content = tf.read_text(encoding="utf-8")
        meta = parse_front_matter(content)
        if "category" not in meta:
            continue
        cat = meta["category"]
        title = meta.get("title") or get_h1(tf)
        categories.setdefault(cat, []).append((title, tf.name))

    for cat in categories:
        categories[cat].sort(key=lambda x: x[0])

    known = [c for c in category_order if c in categories]
    unknown = sorted(c for c in categories if c not in category_order)

    sections = []
    for cat in known + unknown:
        terms = [f"[{title}]({filename})" for title, filename in categories[cat]]
        sections.append(f"## {cat}\n\n" + " · ".join(terms))

    original = index_path.read_text(encoding="utf-8")
    new_body = "\n\n".join(sections) + "\n"
    updated = re.sub(
        r"^## .+",
        new_body,
        original,
        count=1,
        flags=re.DOTALL | re.MULTILINE,
    )

    rel = index_path.relative_to(REPO_ROOT)
    if updated != original:
        index_path.write_text(updated, encoding="utf-8")
        print(f"Updated {rel}")
    else:
        print(f"{rel}: no changes")


def update_category_indexes(docs_dir: Path, cat_dir_map: dict[str, str]) -> None:
    """
    Regenerate the term bullet list in each category index.md.
    Keeps the heading and description; replaces everything from the first list item.
    """
    term_files = sorted(
        f for f in docs_dir.iterdir()
        if f.suffix == ".md" and f.name not in NON_TERM_FILES and f.is_file()
    )

    categories: dict[str, list[tuple[str, str]]] = {}
    for tf in term_files:
        content = tf.read_text(encoding="utf-8")
        meta = parse_front_matter(content)
        if "category" not in meta:
            continue
        cat = meta["category"]
        title = meta.get("title") or get_h1(tf)
        categories.setdefault(cat, []).append((title, tf.name))

    for cat in categories:
        categories[cat].sort(key=lambda x: x[0])

    for cat_label, terms in categories.items():
        cat_dir_name = cat_dir_map.get(cat_label)
        if not cat_dir_name:
            continue
        index_path = docs_dir / cat_dir_name / "index.md"
        if not index_path.exists():
            continue

        original = index_path.read_text(encoding="utf-8")
        new_list = "\n".join(f"- [{title}](../{fname})" for title, fname in terms) + "\n"

        # Replace from first list item to end of file
        updated = re.sub(r"(?ms)^- \[.*", new_list, original, count=1)

        rel = index_path.relative_to(REPO_ROOT)
        if updated != original:
            index_path.write_text(updated, encoding="utf-8")
            print(f"Updated {rel}")
        else:
            print(f"{rel}: no changes")


def update_concept_map(full_nav: list[dict]) -> None:
    """Regenerate the full overview mindmap in docs/concept-maps.md."""
    if not CONCEPT_MAPS_MD.exists():
        print("docs/concept-maps.md: not found, skipping")
        return

    lines = [
        "```mermaid",
        "mindmap",
        "  root((Agentic Software Modernization))",
    ]

    for item in full_nav:
        for label, entries in item.items():
            if not isinstance(entries, list):
                continue
            terms = [name for entry in entries if isinstance(entry, dict)
                     for name in entry]
            if terms:
                lines.append(f"    {label}")
                for term in terms:
                    lines.append(f"      {term}")

    lines.append("```")
    new_block = "\n".join(lines) + "\n"

    original = CONCEPT_MAPS_MD.read_text(encoding="utf-8")
    pattern = r"```mermaid\nmindmap\n  root\(\(Agentic Software Modernization\)\).*?```"
    matches = list(re.finditer(pattern, original, flags=re.DOTALL))

    if not matches:
        print("docs/concept-maps.md: no overview mindmap found, skipping")
        return

    last = matches[-1]
    updated = original[:last.start()] + new_block + original[last.end() + 1:]

    if updated != original:
        CONCEPT_MAPS_MD.write_text(updated, encoding="utf-8")
        print("Updated docs/concept-maps.md")
    else:
        print("docs/concept-maps.md: no changes")


if __name__ == "__main__":
    nav_categories = scan_categories_flat(DOCS_DIR, CATEGORY_ORDER)
    full_nav = update_mkdocs_nav(nav_categories)
    update_mkdocs_de_nav(nav_categories)
    update_index(DOCS_DIR, INDEX_MD, CATEGORY_ORDER)
    de_order = [CATEGORY_LABEL_DE.get(c, c) for c in CATEGORY_ORDER]
    update_index(DOCS_DE_DIR, INDEX_DE_MD, de_order)
    update_category_indexes(DOCS_DIR, CATEGORY_DIR)
    update_category_indexes(DOCS_DE_DIR, CATEGORY_DIR_DE)
    update_concept_map(full_nav)
    print("Done.")
