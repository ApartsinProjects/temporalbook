#!/usr/bin/env python
"""Cross-Reference Architect pass.

During incremental build, forward cross-references were routed to toc.html
(a safe non-broken fallback) because their target chapters did not exist yet.
Now that the whole book exists, repoint each toc-routed link whose ANCHOR TEXT
names a real target to that target's actual file. Links whose anchor text is a
genuine "Contents"/"Table of Contents" reference, or does not name a locatable
target, are left pointing at toc.html.

Matched anchor patterns (case-insensitive):
  - "Chapter N"            -> that chapter's index.html
  - "Section N.M"          -> that section file
  - "Appendix X" (A-G)     -> that appendix's index.html
  - an exact chapter title -> that chapter's index.html

Only <a ...href="...toc.html">ANCHOR</a> links are touched. Header nav, footer
Contents links, and chapter-nav "next -> Contents" links keep anchor text like
"Contents"/"Table of Contents" and are therefore never repointed.
"""
import pathlib
import re
import os

ROOT = pathlib.Path(__file__).resolve().parent.parent

# number -> module path (relative to ROOT), from disk
NUM2MOD = {}
for p in ROOT.glob("part-*/module-*/index.html"):
    m = re.match(r"module-(\d+)-", p.parent.name)
    if m:
        NUM2MOD[int(m.group(1))] = p.parent.relative_to(ROOT).as_posix()

# appendix letter -> path
APPX = {}
for p in ROOT.glob("appendices/*/index.html"):
    m = re.match(r"([A-G])-", p.parent.name)
    if m:
        APPX[m.group(1)] = p.parent.relative_to(ROOT).as_posix() + "/index.html"

# chapter title -> number, parsed from toc.html
TITLE2NUM = {}
toc = (ROOT / "toc.html").read_text(encoding="utf-8")
for m in re.finditer(
        r'toc-chapter-num">(\d+)</span>.*?toc-chapter-title">([^<]+)</span>',
        toc, re.DOTALL):
    TITLE2NUM[m.group(2).strip()] = int(m.group(1))

A_RE = re.compile(r'<a([^>]*?)href="((?:\.\./)+toc\.html)"([^>]*)>(.*?)</a>',
                  re.IGNORECASE | re.DOTALL)
CH_RE = re.compile(r'\bChapter\s+(\d{1,2})\b', re.IGNORECASE)
SEC_RE = re.compile(r'\bSection\s+(\d{1,2})\.(\d{1,2})\b', re.IGNORECASE)
APX_RE = re.compile(r'\bAppendix\s+([A-G])\b', re.IGNORECASE)


def rel(target_rel: str, from_file: pathlib.Path) -> str:
    target = (ROOT / target_rel).resolve()
    return os.path.relpath(target, start=from_file.parent).replace(os.sep, "/")


def resolve(anchor_text: str):
    """Return a ROOT-relative target path for an anchor, or None."""
    plain = re.sub(r"<[^>]+>", "", anchor_text)
    # skip genuine contents links
    if re.search(r"\b(table of contents|contents)\b", plain, re.IGNORECASE):
        return None
    m = SEC_RE.search(plain)
    if m:
        ch, sec = int(m.group(1)), m.group(0).split()[1]
        if ch in NUM2MOD:
            f = f"{NUM2MOD[ch]}/section-{sec}.html"
            if (ROOT / f).exists():
                return f
            return f"{NUM2MOD[ch]}/index.html"
    m = CH_RE.search(plain)
    if m:
        ch = int(m.group(1))
        if ch in NUM2MOD:
            return f"{NUM2MOD[ch]}/index.html"
    m = APX_RE.search(plain)
    if m and m.group(1).upper() in APPX:
        return APPX[m.group(1).upper()]
    t = plain.strip()
    if t in TITLE2NUM and TITLE2NUM[t] in NUM2MOD:
        return f"{NUM2MOD[TITLE2NUM[t]]}/index.html"
    return None


def fix_file(f: pathlib.Path) -> int:
    txt = f.read_text(encoding="utf-8", errors="replace")
    n = 0

    def repl(mt):
        nonlocal n
        pre, href, post, anchor = mt.groups()
        # never touch the chapter-nav "next" link or header/footer nav
        if 'class="next"' in pre or 'class="up"' in pre or 'class="prev"' in pre:
            return mt.group(0)
        if 'toc-link' in pre or 'book-title-link' in pre:
            return mt.group(0)
        tgt = resolve(anchor)
        if not tgt:
            return mt.group(0)
        n += 1
        return f'<a{pre}href="{rel(tgt, f)}"{post}>{anchor}</a>'

    new = A_RE.sub(repl, txt)
    if n:
        f.write_text(new, encoding="utf-8")
    return n


def main():
    files = [p for p in ROOT.rglob("*.html")
             if not any(x in str(p) for x in ("VisionBook", "archive", "templates"))
             and p.name != "toc.html"]
    total = 0
    touched = 0
    for f in files:
        c = fix_file(f)
        if c:
            total += c
            touched += 1
    print(f"Chapters mapped: {len(NUM2MOD)} | appendices: {len(APPX)} | "
          f"titles: {len(TITLE2NUM)}")
    print(f"Repointed {total} cross-references across {touched} files.")


if __name__ == "__main__":
    main()
