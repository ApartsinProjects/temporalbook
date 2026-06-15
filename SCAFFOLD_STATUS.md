# Scaffold Status: Building Temporal AI

Snapshot of the taibook project scaffold. **Scaffolded, not yet built.** No chapter
content has been generated. This file records what exists and the exact next steps for
the content-build phase.

## Style/format basis
Cloned from the sibling book **Building Vision AI** (visionbook.apartsin.com), same
authors and same `book-skills` pipeline. taibook reuses VisionBook's stylesheet,
22-type callout system, KaTeX+Prism vendor stack, templates, and house style verbatim,
so the two books are visually identical.

## What exists now (scaffold)

| Item | Status | Path |
|------|--------|------|
| Editorial plan (9 parts / 36 ch / 7 app) | done | `BOOK_PLAN.md` |
| Pipeline config | done | `BOOK_CONFIG.md` |
| Cross-reference / temporal-thread map | done | `CROSS_REFERENCE_MAP.md` |
| Conformance checklist (house style) | done | `CONFORMANCE_CHECKLIST.md` |
| Directory tree (9 parts, 36 modules + images/) | done | `part-*/module-*/` |
| Appendix dirs (A-G) | done | `appendices/` |
| front-matter / capstone dirs | done | `front-matter/`, `capstone/` |
| Shared stylesheet + 22 callout icons | copied | `styles/` |
| KaTeX + Prism vendor | copied | `vendor/` |
| HTML templates (section, chapter, part) | copied | `templates/` |
| Runtime + audit/build scripts | copied | `scripts/` |
| Previous plain plan | archived | `archive/plan.v1.2026-06-15.txt` |

## What does NOT exist yet (build phase)

- No `section-N.M.html` content files (the actual chapters).
- No `index.html` (book landing), `toc.html` (detailed contents), part `index.html`, or chapter `index.html` pages.
- No front-matter pages (preface, how-to-read, author cards), no appendix content, no capstone.
- No generated illustrations (gemini-imagegen wave) or inline SVG diagrams.
- No bibliographies, epigraphs, or cross-reference links inserted.

## Build phase: how to run it

The build uses the **book-skills** pipeline (46-agent team, 23 stages) per chapter.
Recommended order:

1. **Per-chapter section outlines.** Expand each chapter in `BOOK_PLAN.md` into a
   `chapter-plan.md` inside its module dir (Phase 0, Chapter Lead). Decide section count
   per chapter (target 5-7 sections, matching VisionBook density).
2. **Navigation skeleton.** Generate `index.html`, `toc.html`, the 9 part `index.html`,
   and 36 chapter `index.html` via the Structural Architect (#19), so cross-links resolve
   before content is written.
3. **Chapter production.** Run the full pipeline per chapter, partitioned by the batches
   in `BOOK_CONFIG.md` (A-F). Two agents never edit the same file at once.
4. **Illustrations.** Run the Illustrator (#36) from the main context (needs Bash for
   gemini-imagegen), 5-8 images per chapter.
5. **QA gates.** `scripts/audit_book.py` (adapt canaries for taibook) + `scripts/run_audit.cmd`
   (150 P0-P3 checks). Validate citations with `bibtest`.
6. **Publish pipeline.** `html2epub` -> EPUB 3, then `epub2kpf` -> KDP-ready KPF.

> Batch-First gate: any whole-part or whole-book generation pass must state the
> "Batch API: yes/no" decision line before launching (see book-skills global rule 13).

## Decisions locked (2026-06-15)

- **Density**: deep, ~7 sections/chapter (~250 sections total).
- **Narrative**: rotate all three running datasets (finance / healthcare / sensor-IoT) by part.
- **Deployment**: GitHub Pages + custom domain (mirroring VisionBook) AND Amazon KDP (html2epub -> epub2kpf). HTML must satisfy KDP P0 blockers from the start.

## Still open (optional, can decide at build time)

- Custom domain name (suggest `temporalbook.apartsin.com`).
- Whether to add a companion graduate-course alignment hook (as VisionBook Part IV has).
