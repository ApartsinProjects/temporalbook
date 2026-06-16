# Ready to Submit: Building Temporal AI

Everything KDP needs is in this folder. Validation is green: Kindle Previewer 3
reports **Conversion Success, Enhanced Typesetting Supported, 0 errors, 0 quality
issues** (see `_proof_Summary_Log.csv` / `_proof_QualityReport.csv`).

## Upload (https://kdp.amazon.com -> Bookshelf -> Create -> Kindle eBook)

| KDP step | File / value |
|---|---|
| **Manuscript** | `building-temporal-ai.kpf` (preferred) or `building-temporal-ai.epub` (reflowable; KDP also accepts this and converts server-side) |
| **Cover** | `cover_kdp.jpg` (1600 x 2560 baseline JPEG) |
| **Description** | paste `description.txt` (or the HTML in `description.html`) |
| **Title** | Building Temporal AI |
| **Subtitle** | From Forecasting to Sequential Decision Making |
| **Edition** | 2 |
| **Author** | Alexander Apartsin |
| **Contributor** | Yehudit Aperstein (Author) |
| **Keywords (7)** | see `metadata.yaml` -> `keywords` |
| **Categories (3 BISAC)** | COM004000 (AI/General), COM062000 (Data Science), MAT029000 (Probability & Statistics / Time Series) |
| **Publishing rights** | I own the copyright and hold publishing rights |
| **AI content** | Disclose per KDP policy: AI-generated illustrations (cover + figures) and AI-assisted text, author-reviewed |
| **DRM** | recommended: off |
| **Price / territories** | set at upload (70% royalty needs list price 2.99-9.99 USD) |

## Files in this folder

| File | Purpose |
|---|---|
| `building-temporal-ai.kpf` | manuscript (Kindle package, ET supported, 0 errors) |
| `building-temporal-ai.epub` | manuscript (reflowable EPUB 3, alternative) |
| `cover_kdp.jpg` | cover, 1600 x 2560 baseline sRGB JPEG |
| `description.txt` | plain-text description to paste |
| `description.html` | same description with KDP-allowed HTML |
| `metadata.yaml` | full field reference (title/subtitle/keywords/categories/identifier) |
| `_proof_Summary_Log.csv` | Kindle Previewer verdict: Success / ET Supported / 0 / 0 |
| `_proof_QualityReport.csv` | "Quality checks completed. No issues found." |

## Identifier
EPUB dc:identifier `urn:uuid:85914f1c-f1a9-4240-b74d-9553dd44bb26`. ISBN optional;
leave blank to get a free KDP ASIN.
