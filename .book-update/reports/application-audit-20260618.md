# Application Coverage Audit - Building Temporal AI - 2026-06-18

Scope: audit the book against ten application families where researchers and developers might use it as a main reference. This is a planning artifact only. No book sections were edited.

Skill used: `book-update`, scout mode guidance. Batch API: no, because this was a targeted application planning audit, not a whole-book rewrite or bulk generation pass.

## Executive Verdict

The book is already a strong general Temporal AI reference. It covers the core stack that every application family needs: leakage-safe temporal data engineering, classical forecasting, spectral methods, state-space filtering, anomaly detection, deep sequence models, temporal foundation models, uncertainty, online adaptation, sequential decision making, temporal agents, spatio-temporal intelligence, trustworthiness, deployment, and industrial applications.

It is not yet sufficient as the main reference for leading researchers and developers in all ten application areas. It can become that with a focused application-depth pass. The weakest areas are not core temporal modeling; they are domain-specific frontier layers: limit-order-book finance, supply chain planning as its own application, cybersecurity and fraud, Earth-system foundation models, graph-based anomaly detection, domain benchmarks, regulatory constraints, and decision-value evaluation.

## Sources Scouted

- Time-series foundation model taxonomy and tasks: [Foundation Models for Time Series: A Survey](https://arxiv.org/html/2504.04011v1)
- Financial time-series foundation models: [Time Series Foundation Models for Multivariate Financial Time Series Forecasting](https://arxiv.org/abs/2507.07296)
- Medical time-series foundation model frontier: [MIRA: Medical Time Series Foundation Model for Real-World Health Data](https://openreview.net/forum?id=Auy2DmlJBO)
- Demand forecasting foundation models: [Foundation Models for Demand Forecasting via Dual-Strategy Ensembling](https://arxiv.org/html/2507.22053v1)
- Spatio-temporal foundation models: [Foundation Models for Spatio-Temporal Data Science](https://arxiv.org/html/2503.13502v1)
- Real-world robotics deep RL: [Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes](https://www.annualreviews.org/content/journals/10.1146/annurev-control-030323-022510)
- Earth-system foundation models: [A foundation model for the Earth system](https://www.nature.com/articles/s41586-025-09005-y)
- AI agent architecture and evaluation: [AI Agents: Evolution, Architecture, and Real-World Applications](https://arxiv.org/html/2503.12687v1)
- Foundation models for anomaly detection: [Foundation Models for Anomaly Detection: Vision and Challenges](https://arxiv.org/html/2502.06911v1)
- Weather and climate foundation models: [Deep Learning and Foundation Models for Weather Prediction](https://arxiv.org/html/2501.06907v1)
- Energy load TSFM benchmark: [Time Series Foundation Models for Energy Load Forecasting on Consumer Hardware](https://arxiv.org/pdf/2602.10848)

## Top 10 Application Audit

| Rank | Application family | Current coverage | Researcher-grade gap | Improvement plan |
|---|---|---|---|---|
| 1 | Financial AI and algorithmic trading | Strong coverage of leakage, backtesting, volatility, GARCH, VaR, probabilistic forecasting, foundation models, and finance application section. Evidence: `section-35.1.html`, `section-6.5.html`, `section-2.6.html`, `section-19.*`. | Missing depth on limit-order-book data, market microstructure, execution, market impact, transaction costs beyond simple examples, portfolio construction, model-risk governance, and offline RL for trading. Keyword check found `limit order: 0`. | Add a finance expansion to Section 35.1: LOB and microstructure mini-module, market-impact and execution case, construct-matched backtest audit, portfolio decision layer, and a TSFM finance benchmark callout anchored to recent finance TSFM work. |
| 2 | Clinical and healthcare temporal AI | Strong coverage of irregular sampling, MNAR missingness, clinical early warning, survival, calibration, privacy, fairness, POMDPs, and treatment policy framing. Evidence: `section-35.2.html`, `section-2.3.html`, `section-18.4.html`, `section-23.*`, `section-33.*`. | Needs more on clinical foundation models, external validation, site shift, FHIR or OMOP data schemas, clinical label leakage, treatment-effect estimation with time-varying confounding, and prospective deployment evaluation. | Expand Section 35.2 with a clinical foundation model case around MIRA-style irregular EHR modeling, add a "clinical data contracts" subsection, and add an end-to-end external validation checklist. |
| 3 | Industrial predictive maintenance | Good coverage of spectral analysis, anomaly detection, change points, run-to-failure, survival, cost asymmetry, online monitoring, and deployment. Evidence: `section-35.3.html`, `section-4.*`, `section-8.5.html`, `section-18.4.html`, `section-34.*`. | Needs deeper fleet-level domain adaptation, RUL benchmark landscape, physics-informed digital twins, foundation models for machine health, and maintenance scheduling as optimization under uncertainty. | Add an RUL and fleet adaptation subsection to Section 35.3, add a digital-twin bridge to world models, and add a maintenance scheduling case that evaluates cost avoided rather than detection AUC. |
| 4 | Energy, grid, and climate intelligence | Solid coverage of load forecasting, renewable uncertainty, climate and weather fields, probabilistic intervals, and decision value. Evidence: `section-35.4.html`, `section-19.*`, `section-32.*`. | Needs more on grid operations, optimal power flow, demand response, battery dispatch, probabilistic reserve decisions, and modern Earth-system models such as Aurora. Keyword check found `Aurora: 1`; `load forecasting: 3`. | Expand Section 35.4 with an energy systems decision layer: load forecast to dispatch, reserve, battery, or procurement. Add an Earth-system foundation model frontier box and a benchmark table for zero-shot load TSFMs. |
| 5 | Supply chain and demand forecasting | Partial coverage through demand examples, inventory policy, cold-start retail, hierarchical data, known-future promotions, TFT, TiDE, and foundation models. Evidence: `section-1.3.html`, `section-14.3.html`, `section-14.6.html`, `section-15.3.html`, Appendix E. | This is under-positioned. Keyword check found `supply chain: 1`. Missing dedicated treatment of probabilistic demand planning, intermittent demand, hierarchical reconciliation, inventory optimization, digital twins, service levels, stockout versus holding costs, and promotion or price causal effects. | Add a new Section 35.7, "Supply Chain, Retail Demand, and Inventory Decisions". Make it a full application section with M5-style hierarchy, intermittent demand, quantile safety stock, forecast-to-order optimization, and foundation models for cold start. |
| 6 | Autonomous robotics and control | Strong coverage of MDPs, POMDPs, control, LQR, LQG, imitation, offline RL, Decision Transformers, world models, and robotics application section. Evidence: Part VI and `section-35.5.html`. | Needs more on vision-language-action policies, sim-to-real, real-world robotics failure modes, safety filters, latency budgets, and world model evaluation for planning, causality, and long-horizon consistency. | Expand Section 35.5 and Chapter 29 with VLA and world-action model boxes, add sim-to-real and safety-filter diagrams, and include a world-model planning benchmark sidebar. |
| 7 | Spatio-temporal urban intelligence | Strong foundation in spatio-temporal data, temporal graphs, traffic and mobility concepts, and Part VII spatio-temporal chapter. Evidence: `section-1.4.html`, Chapter 18, Chapter 32. | Needs more on spatio-temporal foundation models, trajectory-powered mobility models, uncertainty-aware mobility forecasting, and urban decision loops such as routing, ride-share balancing, and transit control. | Expand Chapter 32 with a modern STFM section: graph temporal pretraining, traffic foundation models, mobility trajectory foundation models, and a case from forecast to intervention. |
| 8 | Cybersecurity and fraud detection | Current book has useful building blocks: anomaly detection, graph/event modeling, fraud examples, as-of feature stores, online drift, alert fatigue, and monitoring. Evidence: `section-8.5.html`, `section-2.7.html`, Chapter 18. | As a domain reference, it is weak. Keyword check found `cyber: 1`. Missing intrusion detection, log sequence modeling, temporal graph fraud, adversarial adaptation, attack kill chains, account takeover, label delay, and investigation workflows. | Add a dedicated cybersecurity and fraud application section, likely Section 35.8 or a Chapter 35 expansion. Cover event logs, temporal graphs, graph anomaly detection, label delay, adversaries, and explanation for analysts. |
| 9 | AI agents with memory and planning | Strong conceptual coverage of temporal agents, memory, tool use, uncertainty, world models, sequential decisions, and foundation agents. Evidence: Chapter 31, Chapter 29, Section 36.3. | Needs more current depth on long-horizon agent memory benchmarks, tool-use evaluation, agentic workflow monitoring, cost or latency efficiency, and memory governance. | Expand Chapter 31 with a 2026 agent memory section: short-term versus long-term memory, episodic versus semantic stores, memory evals, forgetting, privacy, and cost-aware planning. |
| 10 | Scientific and environmental forecasting | Good coverage of scientific discovery, governing equation recovery, climate/weather fields, causal discovery, uncertainty, and spatio-temporal modeling. Evidence: `section-35.6.html`, `section-35.4.html`, Chapter 30, Chapter 32. | Needs a clearer split between scientific discovery and operational environmental forecasting. Missing dedicated treatment of Earth-system foundation models, extreme events, data assimilation with learned models, physics constraints, and epidemic forecasting as a policy domain. | Expand Sections 35.4 and 35.6 with Earth-system foundation models, extreme-event uncertainty, hybrid physical plus learned models, and an epidemic forecasting mini-case tied to policy evaluation. |

## Cross-Cutting Gaps

### P0: Add missing application sections

1. Add `Section 35.7: Supply Chain, Retail Demand, and Inventory Decisions`.
2. Add `Section 35.8: Cybersecurity, Fraud, and Temporal Security Operations`.

These two are the clearest holes relative to the top-10 list. The book already has the ingredients, but researchers and developers in those domains need domain-native sections, benchmarks, metrics, and failure modes.

### P1: Deepen existing application sections

1. Section 35.1 Finance: add LOB, microstructure, execution, portfolio construction, market impact, transaction costs, and model-risk governance.
2. Section 35.2 Healthcare: add MIRA-style clinical foundation models, FHIR/OMOP, external validation, prospective evaluation, site shift, and time-varying treatment effects.
3. Section 35.3 Predictive Maintenance: add fleet adaptation, RUL benchmarks, physics-informed digital twins, and maintenance scheduling.
4. Section 35.4 Energy and Climate: add grid operations, battery dispatch, demand response, Earth-system foundation models, and zero-shot TSFM load benchmarks.
5. Section 35.5 Robotics: add VLA policies, sim-to-real, safety filters, and world model planning evaluation.
6. Section 35.6 Scientific Discovery: add Earth-system, epidemic, and mechanistic hybrid modeling examples.

### P1: Strengthen frontier coverage in core chapters

1. Chapter 15 should explicitly mention finance-specific, medical-specific, demand-specific, energy-specific, and spatio-temporal foundation models as domain adaptation examples.
2. Chapter 18 should include graph-based time-series anomaly detection and temporal fraud graphs.
3. Chapter 31 should include 2026 memory and long-horizon agent evaluation patterns.
4. Chapter 32 should include spatio-temporal foundation models and trajectory-powered mobility foundation models.
5. Chapter 34 should include domain-specific serving constraints: clinical audit logs, grid latency, trading surveillance, robot control loops, and security incident review workflows.

### P2: Add application benchmark tables

Each application section should end with a compact "researcher benchmark map":

- representative public datasets
- target tasks
- metrics
- leakage traps
- classical baselines
- deep baselines
- foundation model candidates
- decision-value metric

Suggested benchmark anchors:

- Finance: realized volatility, LOBSTER or FI-2010, portfolio and execution simulations.
- Healthcare: MIMIC, eICU, PhysioNet, OMOP-style longitudinal records.
- Predictive maintenance: NASA C-MAPSS, IMS bearing, SMD, SWaT, WADI.
- Energy: electricity transformer temperature, smart meter load, renewable generation, weather reanalysis.
- Supply chain: M5, Favorita, intermittent demand datasets, synthetic promotion and price panels.
- Robotics: D4RL, RLBench, Meta-World, RoboMimic, robot manipulation logs.
- Urban: METR-LA, PEMS, taxi or bike-share trips, mobility traces.
- Cyber/fraud: LANL auth logs, CERT insider threat, credit-card fraud, phishing or bot sequence logs.
- Agents: WebArena, OSWorld, long-horizon tool-use suites, memory benchmarks.
- Scientific/environmental: ERA5, WeatherBench, epidemiological surveillance datasets, gene-expression time courses.

## Recommended Work Plan

### Phase 1: Application Backbone

Add the two missing application sections: supply chain and cybersecurity. This immediately makes the top-10 application promise credible.

### Phase 2: Frontier Refresh

Refresh Chapter 15, Chapter 31, Chapter 32, and Sections 35.1 to 35.6 with short frontier boxes tied to 2025 to 2026 sources. Keep the additions compact: each should explain the new frontier, its relation to the book's existing machinery, and the operational caution.

### Phase 3: Researcher Benchmark Layer

Add benchmark tables to all ten application sections. This is the main thing that changes the book from "broad textbook" to "main reference for application researchers".

### Phase 4: Decision-Value Case Studies

For each application, add one mini-case where the forecast feeds a real decision and is scored by value, not only prediction error. Examples: trading position, sepsis alert threshold, maintenance dispatch, battery dispatch, reorder quantity, robot action, traffic control, fraud investigation queue, agent tool plan, or epidemic intervention.

### Phase 5: Cross-Reference Mesh

Add explicit cross-reference callouts from each application back to the core chapters it uses. The book already has the core material; the improvement is making the path obvious to a domain reader.

## Overall Readiness Scores

| Application | Current readiness as main reference | After plan |
|---|---:|---:|
| Financial AI | 7.5/10 | 9/10 |
| Healthcare temporal AI | 8/10 | 9.5/10 |
| Predictive maintenance | 8/10 | 9.5/10 |
| Energy and climate | 7.5/10 | 9/10 |
| Supply chain and demand | 6/10 | 9/10 |
| Robotics and control | 8/10 | 9.5/10 |
| Urban spatio-temporal intelligence | 7/10 | 9/10 |
| Cybersecurity and fraud | 5/10 | 9/10 |
| Temporal agents | 8/10 | 9.5/10 |
| Scientific and environmental forecasting | 7/10 | 9/10 |

## Final Recommendation

Do not rewrite the whole book. The core spine is already strong. The highest-leverage move is an application-depth layer: two new sections, six expanded sections, four core frontier updates, and benchmark tables across all ten application families.
