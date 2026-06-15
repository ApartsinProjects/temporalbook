#!/usr/bin/env python
"""Activate a built chapter in the navigation: flip its toc.html and part-index
entries from plain text to live links. Reusable for every chapter as it ships.

Usage:
  python scripts/activate_chapter.py \
     --chapter 2 \
     --title "Temporal Data Engineering" \
     --modpath part-1-foundations/module-02-temporal-data-engineering \
     --part-index part-1-foundations/index.html

The chapter title must match exactly the text inside the toc <span class="toc-chapter-title">
and the part-index chapter card header. Section links are derived from the section
files present on disk in the module directory.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def activate_toc(chapter, title, modpath):
    toc = ROOT / "toc.html"
    txt = toc.read_text(encoding="utf-8")
    moddir_url = modpath  # toc links are relative to root

    # 1. chapter title span -> card link (drop the in-production badge)
    old_title = (f'<span class="toc-chapter-title">{title}</span> '
                 f'<span class="status-pending">in production</span>')
    new_title = (f'<a class="toc-card-link" href="{moddir_url}/index.html">'
                 f'<span class="toc-chapter-title">{title}</span></a>')
    if old_title not in txt:
        print(f"  WARN: toc chapter title for '{title}' not found (already active?)")
    else:
        txt = txt.replace(old_title, new_title, 1)

    # 2. each plain section <li> for this chapter -> wrap text in a sec-link
    def wrap_section(m):
        num, text = m.group(1), m.group(2).strip()
        fn = f"{moddir_url}/section-{num}.html"
        if not (ROOT / f"{modpath}/section-{num}.html").exists():
            return m.group(0)  # leave as-is if file missing
        return (f'<li><span class="toc-section-num">{num}</span> '
                f'<a class="toc-sec-link" href="{fn}">{text}</a></li>')

    sec_re = re.compile(
        rf'<li><span class="toc-section-num">({chapter}\.\d+)</span>\s+'
        rf'(?!<a)([^<]+)</li>')
    txt, n = sec_re.subn(wrap_section, txt)
    toc.write_text(txt, encoding="utf-8")
    print(f"  toc.html: chapter title linked, {n} section links wired")


def activate_part_index(chapter, title, part_index, moddir):
    pi = ROOT / part_index
    txt = pi.read_text(encoding="utf-8")
    # match the card header line with the in-production badge for this chapter
    pat = re.compile(
        rf'<span class="mod-num">Chapter {chapter}</span> {re.escape(title)} '
        rf'<span class="status-pending"[^>]*>in production</span>')
    repl = (f'<a href="{moddir}/index.html"><span class="mod-num">Chapter '
            f'{chapter}</span> {title}</a>')
    txt, n = pat.subn(repl, txt)
    if n == 0:
        print(f"  WARN: part-index card for Chapter {chapter} not found (already active?)")
    else:
        pi.write_text(txt, encoding="utf-8")
        print(f"  {part_index}: chapter card linked")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--modpath", required=True, help="part-N-slug/module-NN-slug")
    ap.add_argument("--part-index", required=True)
    args = ap.parse_args()
    moddir = args.modpath.split("/")[-1]
    print(f"Activating Chapter {args.chapter}: {args.title}")
    activate_toc(args.chapter, args.title, args.modpath)
    activate_part_index(args.chapter, args.title, args.part_index, moddir)
    print("Done.")


if __name__ == "__main__":
    main()
