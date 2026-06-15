#!/usr/bin/env python
"""Redirect broken internal links to the toc hub.

Agents sometimes hard-link to not-yet-built chapters (forward references) or use
a wrong relative depth. Until the target chapter ships, those links 404. This
fixer rewrites any internal href whose resolved target does not exist to point at
the table of contents (../../toc.html or ../toc.html or toc.html by depth). The
end-of-book Cross-Reference Architect wave repoints these to real files once all
chapters exist.

Usage:
  python scripts/fix_forward_links.py                # whole book
  python scripts/fix_forward_links.py FILE [FILE...] # specific files
External (http), in-page (#...), and already-valid links are left untouched.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HREF = re.compile(r'href="([^"]+)"')


def toc_rel(f: pathlib.Path) -> str:
    depth = len(f.relative_to(ROOT).parts) - 1  # dirs above the file
    return "../" * depth + "toc.html"


def fix_file(f: pathlib.Path) -> int:
    txt = f.read_text(encoding="utf-8", errors="replace")
    toc = toc_rel(f)
    n = 0

    def repl(m):
        nonlocal n
        href = m.group(1)
        if href.startswith(("http://", "https://", "#", "mailto:")):
            return m.group(0)
        path = href.split("#")[0]
        if not path:
            return m.group(0)
        if (f.parent / path).resolve().exists():
            return m.group(0)
        n += 1
        return f'href="{toc}"'

    new = HREF.sub(repl, txt)
    if n:
        f.write_text(new, encoding="utf-8")
    return n


def main():
    if len(sys.argv) > 1:
        files = [pathlib.Path(a) for a in sys.argv[1:]]
    else:
        files = [p for p in ROOT.rglob("*.html")
                 if not any(x in str(p) for x in ("VisionBook", "archive", "templates"))]
    total = 0
    for f in files:
        c = fix_file(f)
        if c:
            print(f"  {f.relative_to(ROOT)}: redirected {c} broken link(s) to toc")
            total += c
    print(f"Total redirected: {total}")


if __name__ == "__main__":
    main()
