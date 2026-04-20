"""
Inject the other-language translation link right after the <h1> of term pages.
Reads translation_en / translation_de front matter and the alternate config to build
the href, then inserts an <a class="translation-link"> after the h1. Kept outside the
h1 so the search index title does not mix English and German terms.
"""

from bs4 import BeautifulSoup


def on_page_content(html, page, config, **kwargs):
    meta = page.meta
    alternates = config.extra.get("alternate", [])

    en_slug = meta.get("translation_en")
    en_title = meta.get("translation_en_title")
    de_slug = meta.get("translation_de")
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

    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if h1 is None:
        return html

    anchor = soup.new_tag("a", href=root + slug + "/")
    anchor["class"] = "translation-link"
    anchor.string = title
    h1.insert_after(anchor)

    return str(soup)
