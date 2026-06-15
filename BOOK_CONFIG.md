# Book Configuration

This file contains all book-specific details for the textbook production pipeline
(the `book-skills` 46-agent team). The pipeline skill and its agent definitions are
generic; this file is the only place where content specific to THIS book lives.
The full editorial plan (parts, chapters, sections, change log) lives in
`BOOK_PLAN.md`; this file is the chapter-level operational source of truth.

## Book Identity

- **Title**: Building Temporal AI: From Forecasting to Sequential Decision Making
- **Subtitle**: A Practitioner's Guide to Time Series, Temporal Deep Learning, Foundation Models, and Sequential Decision Making
- **Authors**: Alexander Apartsin & Yehudit Aperstein
- **Target Audience**: Senior undergraduates, graduate students, researchers, and practitioners with linear algebra, probability, calculus, and introductory machine learning. No prior time-series experience required; appendices A-D provide refreshers.
- **Output Format**: HTML chapter files linking to the shared stylesheet `styles/book.css`
- **Author/Footer line**: `© 2026 Alexander Apartsin · <a href="../../toc.html">Contents</a>` (adjust relative depth per file location)
- **Edition line for footers**: `Building Temporal AI: From Forecasting to Sequential Decision Making, First Edition`
- **Sibling book (style reference)**: Building Vision AI (visionbook.apartsin.com). taibook reuses its callout system, stylesheet, vendor stack, and house style verbatim.

## The Nine-Part Arc

1. **Part I: Foundations of Temporal AI** (Ch 1-2): what makes intelligence temporal, predictability limits, temporal data engineering and leakage.
2. **Part II: Classical Forecasting and Time Series Analysis** (Ch 3-8): statistical foundations, frequency domain, univariate and multivariate/econometric models, state-space filtering, anomaly and change-point detection.
3. **Part III: Temporal Deep Learning** (Ch 9-15): sequence fundamentals, RNNs, TCNs, Transformers, structured state-space and continuous-time models, deep forecasting architectures, temporal foundation models.
4. **Part IV: Temporal Representation Learning** (Ch 16-18): self-supervised and contrastive representations, generative temporal models, event/point-process/temporal-graph modeling.
5. **Part V: Uncertainty, Online, and Adaptive Learning** (Ch 19-21): probabilistic and conformal forecasting, online/continual learning under drift, adaptive systems.
6. **Part VI: Sequential Decision Making** (Ch 22-29): MDPs, POMDPs, bandits and RL foundations, deep and advanced RL, optimal control and imitation, sequences-as-decision-making, world models and planning.
7. **Part VII: Building Intelligent Temporal Systems** (Ch 30-32): temporal reasoning and causality, temporal agents, spatio-temporal intelligence.
8. **Part VIII: Trustworthy and Deployed Temporal AI** (Ch 33-34): interpretability/robustness/fairness/privacy, deployment and MLOps.
9. **Part IX: Applications and Future Directions** (Ch 35-36): industrial applications, toward general temporal intelligence.

A recurring narrative thread (the "temporal thread"): each classical idea returns in
learned form. The Kalman filter (Ch 7) returns as the RNN (Ch 10) and the structured
state-space model (Ch 13); the HMM (Ch 7) returns as the neural latent-variable model
(Ch 17) and the belief-state agent (Ch 23); ARIMA (Ch 5) returns as linear attention
(Ch 13); spectral analysis (Ch 4) returns in frequency-domain forecasters (Ch 14); the
MDP (Ch 22) returns as a sequence model (Ch 28). Agents should exploit these arcs for
cross-references (see CROSS_REFERENCE_MAP.md).

## Visual Style

- **Stylesheet**: every HTML file links `styles/book.css` (full callout system, 22 types). Code highlighting uses Prism (vendor) plus `styles/pygments.css`. Math uses KaTeX (vendor).
- **Illustrations**: inline SVG diagrams with `<figure class="diagram">` and numbered `<figcaption>`. Generated PNG illustrations are a later wave (gemini-imagegen); do not block on them.
- **Application Examples**: `.callout.practical-example` boxes, realistic industry mini-stories (finance, healthcare, manufacturing, energy, robotics).
- **Bibliographies**: card layout on the chapter index page, 8 to 15 hyperlinked annotated entries.
- **Epigraphs**: humorous quotes attributed to a fictional temporal-AI persona, format "A [Adjective] [Temporal Role]".

### Example epigraph personas (temporal-flavored)

- "A Recurrent Network With Long-Term Commitment Issues"
- "An Autoregressive Model Predicting Its Own Downfall"
- "A Kalman Filter That Trusts the Measurement Too Much"
- "A Mildly Overfit Forecaster, Confident About Next Tuesday"
- "An Attention Head Stuck in the Past"
- "A Reinforcement Learner Still Exploring"
- "A Non-Stationary Process Having an Identity Crisis"
- "A Concept Drift Detector Who Has Seen Regimes Come and Go"
- "A Hidden Markov Model Keeping Its States to Itself"
- "A Decision Transformer Conditioning on a Return It Cannot Reach"

## HTML Head Boilerplate

Section files (`part-*/module-*/section-N.M.html`) use this head:

```html
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="Section N.M: Title. One-sentence description." name="description"/>
<title>Section N.M: Title | Building Temporal AI</title>
<link href="../../styles/book.css" rel="stylesheet"/>
<link href="../../styles/pygments.css" rel="stylesheet"/>
<link href="../../vendor/katex/katex.min.css" rel="stylesheet"/>
<script defer="" src="../../vendor/katex/katex.min.js"></script>
<script defer="" onload="renderMathInElement(document.body, {
  delimiters: [
  {left: '$$', right: '$$', display: true},
  {left: '$', right: '$', display: false}
  ],
  throwOnError: false
  });" src="../../vendor/katex/contrib/auto-render.min.js"></script>
<link href="../../vendor/prism/prism-theme.css" rel="stylesheet"/>
<script defer="" src="../../vendor/prism/prism-bundle.min.js"></script>
<script defer="" src="../../scripts/book.js"></script>
```

Chapter index files (`part-*/module-*/index.html`) use the same `../../` depth.
Part index files (`part-*/index.html`) use `../` depth. Root files use no prefix.

Every page carries the standard header:

```html
<header class="chapter-header">
<nav class="header-nav">
<a class="book-title-link" href="../../index.html">Building Temporal AI: From Forecasting to Sequential Decision Making</a>
<a class="toc-link" href="../../toc.html" title="Table of Contents"><span class="toc-icon">&#9776;</span> Contents</a>
</nav>
<div class="part-label"><a href="../index.html">Part [ROMAN]: [PART TITLE]</a></div>
<div class="chapter-label"><a href="index.html">Chapter [N]: [CHAPTER TITLE]</a></div>
<h1>[SECTION TITLE]</h1>
</header>
```

## Chapter Map (Current Structure)

Module directory numbers equal global chapter numbers (1 to 36). The canonical
section-level breakdown lives in `BOOK_PLAN.md` and (once generated) `toc.html`;
this map is the chapter-level source of truth.

```
Part 1: Foundations of Temporal AI (part-1-foundations/)
  Ch 1: Introduction to Temporal Intelligence        module-01-intro-temporal-intelligence
  Ch 2: Temporal Data Engineering                     module-02-temporal-data-engineering

Part 2: Classical Forecasting and Time Series Analysis (part-2-classical-forecasting/)
  Ch 3: Statistical Foundations                       module-03-statistical-foundations
  Ch 4: Frequency-Domain and Spectral Analysis        module-04-frequency-spectral
  Ch 5: Univariate Forecasting Models                 module-05-univariate-forecasting
  Ch 6: Multivariate and Econometric Models           module-06-multivariate-econometric
  Ch 7: State-Space Models and Filtering              module-07-state-space-filtering
  Ch 8: Temporal Anomaly and Change-Point Detection   module-08-anomaly-changepoint

Part 3: Temporal Deep Learning (part-3-temporal-deep-learning/)
  Ch 9:  Neural Sequence Modeling Fundamentals        module-09-neural-sequence-fundamentals
  Ch 10: Recurrent Neural Networks                     module-10-recurrent-neural-networks
  Ch 11: Temporal Convolutional Networks              module-11-temporal-convolutional-networks
  Ch 12: Attention and Transformers                    module-12-attention-transformers
  Ch 13: State-Space and Continuous-Time Neural Models module-13-ssm-continuous-time
  Ch 14: Deep Forecasting Architectures               module-14-deep-forecasting-architectures
  Ch 15: Temporal Foundation Models                   module-15-temporal-foundation-models

Part 4: Temporal Representation Learning (part-4-temporal-representation-learning/)
  Ch 16: Learning Temporal Representations             module-16-learning-temporal-representations
  Ch 17: Generative Temporal Models                    module-17-generative-temporal-models
  Ch 18: Event and Sequence Modeling                   module-18-event-sequence-modeling

Part 5: Uncertainty, Online, and Adaptive Learning (part-5-uncertainty-online-adaptive/)
  Ch 19: Probabilistic Forecasting and Uncertainty Quantification  module-19-probabilistic-uncertainty
  Ch 20: Online and Continual Learning                 module-20-online-continual-learning
  Ch 21: Adaptive Temporal AI Systems                  module-21-adaptive-systems

Part 6: Sequential Decision Making (part-6-sequential-decision-making/)
  Ch 22: Markov Decision Processes                     module-22-markov-decision-processes
  Ch 23: Partial Observability and POMDPs              module-23-pomdps
  Ch 24: Bandits and Foundations of Reinforcement Learning  module-24-bandits-rl-foundations
  Ch 25: Deep Reinforcement Learning                   module-25-deep-reinforcement-learning
  Ch 26: Advanced Reinforcement Learning               module-26-advanced-rl
  Ch 27: Optimal Control and Imitation Learning        module-27-control-imitation
  Ch 28: Sequence Models for Decision Making           module-28-sequence-models-decision
  Ch 29: World Models and Planning                     module-29-world-models-planning

Part 7: Building Intelligent Temporal Systems (part-7-building-intelligent-systems/)
  Ch 30: Temporal Reasoning and Causality              module-30-temporal-reasoning-causality
  Ch 31: Temporal AI Agents                            module-31-temporal-ai-agents
  Ch 32: Spatio-Temporal Intelligence                  module-32-spatio-temporal

Part 8: Trustworthy and Deployed Temporal AI (part-8-trustworthy-deployed/)
  Ch 33: Interpretability, Robustness, and Responsible Temporal AI  module-33-interpretability-robustness
  Ch 34: Deploying and Operating Temporal AI Systems   module-34-deployment-mlops

Part 9: Applications and Future Directions (part-9-applications-future/)
  Ch 35: Industrial Applications                       module-35-industrial-applications
  Ch 36: Toward General Temporal Intelligence          module-36-general-temporal-intelligence
```

Front matter lives in `front-matter/` (F1-F7), appendices in `appendices/` (A-G),
capstone in `capstone/`. See `BOOK_PLAN.md` for the full section-level plan.

## Appendices

- A: Mathematical Foundations and Unified Notation  (appendices/A-math-foundations)
- B: Probability and Statistics Refresher           (appendices/B-probability-statistics)
- C: Optimization and Deep Learning Basics          (appendices/C-optimization-deep-learning)
- D: PyTorch for Temporal AI (and JAX notes)        (appendices/D-pytorch-temporal)
- E: Datasets, Benchmarks, and Evaluation Protocols (appendices/E-datasets-benchmarks)
- F: Reproducibility, Compute, and Experiment Management  (appendices/F-reproducibility-compute)
- G: Solutions to Selected Exercises                (appendices/G-solutions)

## Relative Path Rules

- Same part: `../module-XX-name/index.html`
- Different part: `../../part-N-name/module-XX-name/index.html`
- To book root from a section file: `../../`

## Three Running Datasets (use across chapters for comparability)

- **Finance**: a returns/volatility series (e.g. equity index or FX). Threads through Ch 5-6 (ARIMA/GARCH), Ch 14 (deep forecasting), Ch 19 (probabilistic forecasting), Ch 35.1.
- **Healthcare**: an irregularly-sampled multivariate clinical series (vitals). Threads through Ch 2 (irregular data), Ch 7 (filtering), Ch 13 (Neural CDE), Ch 18 (time-to-event), Ch 35.2.
- **Sensor/IoT**: industrial telemetry. Threads through Ch 8 (anomaly/change-point), Ch 20 (drift), Ch 32 (spatio-temporal), Ch 34 (deployment), Ch 35.3.

## Batch Partitioning (for parallel agent runs)

- Batch A: Part 1 (Ch 1-2, 2 modules)
- Batch B: Part 2 (Ch 3-8, 6 modules)
- Batch C: Part 3 (Ch 9-15, 7 modules)
- Batch D: Part 4 + Part 5 (Ch 16-21, 6 modules)
- Batch E: Part 6 (Ch 22-29, 8 modules)
- Batch F: Parts 7-9 (Ch 30-36, 7 modules)

Two agents must never edit the same file at overlapping times. One chapter equals
one file set; different chapters may proceed in parallel; agent waves within a
chapter run strictly in sequence.

## Build Decisions (locked 2026-06-15)

- **Section density**: deep, target ~7 sections per chapter (~250 sections across 36 chapters). Matches the "Deeper" tier; exceeds VisionBook density.
- **Running narrative**: rotate all three datasets by part (finance / healthcare / sensor-IoT), as detailed under "Three Running Datasets" above. No single lead domain.
- **Deployment targets**: (1) GitHub Pages with a custom domain (e.g. `temporalbook.apartsin.com`), mirroring VisionBook; (2) Amazon KDP via `html2epub` -> `epub2kpf`. Build all HTML to satisfy both web and KDP/Kindle (P0 blockers) from the start.

## The "Right Tool" Principle

Every section that teaches a concept from scratch must also include a
`.callout.library-shortcut` showing the same task solved in a few lines with a modern
library. State the line-count reduction explicitly and name what the library handles
internally. Canonical temporal-AI toolbox: statsmodels, pmdarica/sktime, Prophet,
Nixtla (statsforecast / neuralforecast / mlforecast), GluonTS, Darts, tslib, PyTorch,
PyTorch Forecasting, Lightning, HuggingFace (Chronos, Lag-Llama, Moirai, TimesFM,
MOMENT), tslearn, river (online learning), Gymnasium, Stable-Baselines3, CleanRL,
d3rlpy (offline RL), tianshou, scikit-learn, NeuralProphet, tsai.

## QA Audit Pipeline

Two complementary gates, both run before any "done" or publish claim:

1. `C:\Python314\python.exe scripts\audit_book.py`: taibook-specific content canaries
   (file completeness vs the chapter map, dash discipline, per-section structure, link
   integrity). Adapt from the VisionBook copy already in `scripts/`.
2. `scripts\run_audit.cmd`: the book-skills audit-plugin pipeline (150 pluggable checks,
   P0-P3), the same system that gates VisionBook and the LLMBook. P0 includes the
   KDP/Kindle blockers (strict XHTML, bare-dollar math, unresolvable font weights).
   Auto-fix scripts live in `E:\Projects\claude-skills\book-skills\scripts\fix\`.
   Book-specific calibration: skip `OFFTOPIC_NO_LLM_CONTEXT` (it tests LLM-book topicality).

## Style Rules (non-negotiable)

1. NEVER use em dashes or double dashes anywhere. Use commas, semicolons, colons, parentheses, or separate sentences.
2. Book hierarchy terminology: Part > Chapter > Section. Never "course", "lecture", "module" in reader-facing prose (directory names keep `module-NN` for tooling compatibility).
3. Every figure, table, code block, and callout must be referenced in surrounding prose.
4. Code captions (`<div class="code-caption">`) go BELOW the code block, are specific, and are unique within a file.
5. Every chapter index ends with a "What's Next" section linking the next chapter, placed before the bibliography.
6. Use `.part-label` (not `.subtitle`) for the Part label in headers.
7. No placeholder text of any kind. Every section ships complete or is not created.
8. Each chapter follows the 9-point pedagogical scaffold from BOOK_PLAN.md (objectives, motivation, exposition, worked examples, classical-neural bridge box, case study, pitfalls, exercises, further reading).
