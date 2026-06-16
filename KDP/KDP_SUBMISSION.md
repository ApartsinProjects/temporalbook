# KDP Submission Guide: Building Temporal AI

Single source of truth for the Kindle Direct Publishing submission. Field values
mirror `KDP/metadata/metadata.yaml` and `html2epub.toml`.

## Deliverables

| Item | Path | Spec |
|---|---|---|
| Manuscript (EPUB 3, reflowable) | `KDP/output/building-temporal-ai.epub` | EPUBCheck 0/0/0; KDP accepts EPUB directly |
| Manuscript (KPF, optional) | `KDP/output/building-temporal-ai.kpf` | Kindle Previewer 3: Enhanced Typesetting supported, 0 errors |
| Cover | `KDP/cover/cover_kdp.jpg` | 1600 x 2560, baseline (non-progressive) sRGB JPEG |

KDP accepts a reflowable EPUB directly and runs its own server-side KFX
conversion. The KPF is for local validation/preview only and is not required
for upload.

## Build commands

```bash
# 1. one-time: install KaTeX for server-side math rendering
cd KDP/build && npm install && cd ../..

# 2. build the reflowable EPUB
python -m html2epub build .                       # -> KDP/output/building-temporal-ai.epub

# 3. regenerate the cover (only if artwork or text changes)
python KDP/cover/composite_cover.py               # -> KDP/cover/cover_kdp.jpg

# 4. (optional) KPF for local Kindle Previewer validation
#    use the epub2kpf skill: rasterize math + diagrams for the Kindle copy,
#    run the kdp_post_build patch chain, then Kindle Previewer 3 -convert.
```

## KDP form fields

### Kindle eBook Details
- **Language:** English
- **Book Title:** Building Temporal AI
- **Subtitle:** From Forecasting to Sequential Decision Making
- **Edition number:** 1
- **Author:** Alexander Apartsin
- **Contributor:** Yehudit Aperstein (Author)
- **Description:** paste the rendered text of `KDP/metadata/description.html`
- **Publishing rights:** I own the copyright and hold the publishing rights
- **Keywords (7):** see `metadata.yaml` `keywords`
- **Categories (up to 3 BISAC):**
  - COMPUTERS / Artificial Intelligence / General (COM004000)
  - COMPUTERS / Data Science / General (COM062000)
  - MATHEMATICS / Probability & Statistics / Time Series (MAT029000)
- **Age range / Reading age:** not applicable (professional / scholarly)

### Kindle eBook Content
- **Manuscript:** upload `KDP/output/building-temporal-ai.epub`
- **Cover:** upload `KDP/cover/cover_kdp.jpg` (or use the same on KDP Cover Creator)
- **AI content:** disclose per current KDP policy. This book contains
  AI-generated illustrations (cover and chapter figures) and AI-assisted text
  that the authors reviewed and edited.

### Kindle eBook Pricing
- **Territories:** All
- **Royalty:** author choice (70% requires list price 2.99-9.99 USD)
- **DRM:** recommendation: do not enable
- **Price:** set at upload

## Pre-upload checklist
- [ ] `python -m html2epub build .` succeeds, EPUB present
- [ ] Structural validation 0 broken internal links
- [ ] Cover is exactly 1600 x 2560, baseline JPEG, RGB
- [ ] Description pasted from `description.html`
- [ ] 7 keywords, 3 categories set
- [ ] Spot-check the EPUB in Kindle Previewer 3 (math, code, figures, TOC)
