"""
Inject the other-language translation link into the <h1> of term pages at build time.
Reads translation_en / translation_de front matter and the alternate config to build
the href, then appends an <a class="translation-link"> before the closing </h1>.
"""

import re
from html import escape


def on_page_content(html, page, config, **kwargs):
    meta = page.meta
    alternates = config.extra.get("alternate", [])

    en_slug  = meta.get("translation_en")
    en_title = meta.get("translation_en_title")
    de_slug  = meta.get("translation_de")
    de_title = meta.get("translation_de_title")

    if en_slug and en_title:
        target_lang, slug, title = "en", en_slug, en_title
    elif de_slug and de_title:
        target_lang, slug, title = "de", de_slug, de_title
    else:
        return html

    root = next(
        (a["link"].rstrip("/") + "/" for a in alternates if a.get("lang") == target_lang),
        None,
    )
    if not root:
        return html

    href = root + slug + "/"
    link = f'<a href="{escape(href)}" class="translation-link">{escape(title)}</a>'

    return re.sub(r"(</h1>)", link + r"\1", html, count=1)
