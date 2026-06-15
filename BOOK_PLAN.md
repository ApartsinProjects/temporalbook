# Building Temporal AI: From Forecasting to Sequential Decision Making

> **Comprehensive graduate-level textbook plan (v2, extended).**
> Supersedes `archive/plan.v1.2026-06-15.txt`. This revision adds the modern
> state-space/continuous-time model family, multivariate and frequency-domain
> classical methods, probabilistic/conformal forecasting and uncertainty
> quantification, partial observability, sequences-as-decision-making, and a
> dedicated part on trustworthy and deployed temporal AI. Structure expands
> from 8 parts / 25 chapters to **9 parts / 36 chapters / 7 appendices**.

---

## Book Description

Time is one of the most fundamental dimensions of intelligence. Whether predicting
stock prices, diagnosing patients from evolving symptoms, controlling autonomous
vehicles, optimizing industrial processes, or enabling intelligent agents to plan
and act, modern AI systems must learn from events that unfold over time.

*Building Temporal AI* provides a comprehensive journey through the theories,
models, and engineering practices required to develop intelligent systems that
understand, predict, and act in dynamic environments. Starting with classical
statistical forecasting methods, the book progressively introduces modern deep
learning architectures, state-space and continuous-time models, representation
learning, temporal foundation models, and reinforcement learning approaches for
sequential decision making, before closing with the engineering, trust, and
deployment concerns that govern real systems.

Unlike traditional time-series books that focus solely on forecasting, this text
presents a unified view of Temporal AI, connecting prediction, reasoning,
planning, and action within a single conceptual framework. A recurring thread
draws explicit bridges between classical and neural methods (Kalman filter ↔ RNN ↔
structured state-space model; ARIMA ↔ linear attention; HMM ↔ neural latent
variable model; MDP ↔ control ↔ sequence model), so the reader leaves with one
mental model rather than a catalogue of tricks.

The book combines mathematical foundations, practical implementations, real-world
case studies, and hands-on examples using modern AI frameworks. It is intended for
senior undergraduate students, graduate students, researchers, and practitioners
seeking to build next-generation AI systems that operate in dynamic and evolving
environments.

**Key topics include:**

* Classical univariate and multivariate time series analysis and forecasting
* Frequency-domain and spectral methods
* State-space models, filtering, and continuous-time neural models
* Temporal deep learning: RNNs, TCNs, Transformers, and structured SSMs (S4/Mamba)
* Deep and probabilistic forecasting architectures
* Self-supervised temporal representation learning
* Temporal foundation models and LLMs for time series
* Event, point-process, and temporal-graph modeling
* Uncertainty quantification and conformal prediction
* Online, continual, and adaptive learning under distribution shift
* Sequential decision making: MDPs, POMDPs, bandits, and reinforcement learning
* Optimal control, imitation learning, and sequences-as-decision-making
* World models, planning, and agentic systems
* Interpretability, robustness, fairness, privacy, and deployment
* Real-world applications across finance, healthcare, robotics, industry, and intelligent agents

**Prerequisites.** Linear algebra, probability, multivariable calculus, and
introductory machine learning. Appendices A–D provide refreshers.

---

## Pedagogical Conventions (apply to every chapter)

Each chapter follows a consistent structure to support graduate teaching and
self-study:

1. **Learning objectives** — 4–6 measurable outcomes opening the chapter.
2. **Motivation & running example** — a concrete problem revisited throughout.
3. **Core exposition** — theory with derivations, intuition, and figures.
4. **Worked examples** — fully solved, with math and minimal code.
5. **Classical ↔ neural bridge box** — explicit link to related methods elsewhere.
6. **Case study** — one real dataset/domain applied end to end.
7. **Pitfalls & practice notes** — leakage, look-ahead bias, common failure modes.
8. **Exercises** — split into *theory*, *implementation*, and *open-ended*.
9. **Further reading & open problems** — curated, current pointers.

**Unified notation.** A single notation table (Appendix A) standardizes symbols
across the ML, control, and statistics traditions, which otherwise clash.

**Running datasets.** Three threads recur across the book for comparability:
a financial series (returns/volatility), a clinical multivariate series
(irregularly sampled vitals), and a sensor/IoT series (industrial telemetry).

---

# Table of Contents

## Part I. Foundations of Temporal AI

### Chapter 1. Introduction to Temporal Intelligence
1.1 What Makes Intelligence Temporal?
1.2 Temporal Data Across Domains
1.3 Prediction, Reasoning, and Decision Making
1.4 Types of Temporal Data (regular, irregular, event, multivariate, spatio-temporal)
1.5 Predictability, Entropy Rate, and the Limits of Forecasting
1.6 Challenges in Temporal Modeling
1.7 The Temporal AI Landscape and How to Read This Book

### Chapter 2. Temporal Data Engineering
2.1 Time Stamps, Time Zones, and Event Ordering
2.2 Sampling, Resampling, and Aggregation
2.3 Missing Data and Irregular Observations
2.4 Feature Engineering for Temporal Data
2.5 Windowing, Segmentation, and Lag Construction
2.6 Evaluation Protocols, Backtesting, and Data Leakage
2.7 Reproducibility and Temporal Data Pipelines

---

## Part II. Classical Forecasting and Time Series Analysis

### Chapter 3. Statistical Foundations
3.1 Random Processes and Ergodicity
3.2 Stationarity and Unit Roots
3.3 Autocorrelation and Partial Autocorrelation
3.4 Trend and Seasonality
3.5 Time-Series Decomposition (classical, STL, robust)

### Chapter 4. Frequency-Domain and Spectral Analysis *(new)*
4.1 Fourier Analysis and the Periodogram
4.2 Spectral Density Estimation
4.3 Filtering in the Frequency Domain
4.4 Wavelets and Time–Frequency Analysis
4.5 Connections to Modern Architectures (frequency mixers, FEDformer)

### Chapter 5. Univariate Forecasting Models
5.1 Moving Average Models
5.2 Autoregressive Models
5.3 ARMA and ARIMA
5.4 SARIMA and Seasonal Modeling
5.5 Exponential Smoothing and ETS
5.6 Prophet and Modern Statistical Frameworks
5.7 Model Selection, Diagnostics, and Information Criteria

### Chapter 6. Multivariate and Econometric Models *(new)*
6.1 Vector Autoregression (VAR) and VARMA
6.2 Granger Causality and Impulse-Response Analysis
6.3 Cointegration and Error-Correction Models
6.4 Dynamic Factor Models
6.5 Volatility Modeling: ARCH, GARCH, and Stochastic Volatility

### Chapter 7. State-Space Models and Filtering
7.1 Hidden States and the State-Space Formulation
7.2 The Kalman Filter
7.3 Extended and Unscented Kalman Filters
7.4 Particle Filters and Sequential Monte Carlo
7.5 Hidden Markov Models
7.6 Bridge: Filtering as Recurrent Inference

### Chapter 8. Temporal Anomaly and Change-Point Detection
8.1 Point, Contextual, and Collective Anomalies
8.2 Statistical and Distance-Based Approaches
8.3 Change-Point Detection (offline and online)
8.4 Forecasting-Residual and Reconstruction Methods
8.5 Industrial and Monitoring Applications

---

## Part III. Temporal Deep Learning

### Chapter 9. Neural Sequence Modeling Fundamentals
9.1 Feedforward Networks for Time Series
9.2 Sequence Learning Concepts and Tasks
9.3 Backpropagation Through Time
9.4 Long-Term Dependencies and Gradient Pathologies

### Chapter 10. Recurrent Neural Networks
10.1 Vanilla RNNs
10.2 LSTM Networks
10.3 GRU Networks
10.4 Encoder–Decoder and Seq2Seq Architectures
10.5 Bridge: RNNs as Learned Kalman Filters
10.6 Practical Considerations and Training Stability

### Chapter 11. Temporal Convolutional Networks
11.1 One-Dimensional Convolutions
11.2 Dilated and Causal Convolutions
11.3 Temporal Convolutional Networks (TCN)
11.4 WaveNet
11.5 Comparative Analysis (RNN vs TCN vs Transformer)

### Chapter 12. Attention and Transformers
12.1 Self-Attention
12.2 The Transformer Architecture
12.3 Positional and Temporal Encodings
12.4 Long-Sequence Modeling and Memory
12.5 Efficient and Sparse Transformers

### Chapter 13. State-Space and Continuous-Time Neural Models *(new)*
13.1 From HiPPO to Structured State-Space Models (S4, S5)
13.2 Selective State-Space Models (Mamba) and Hardware-Aware Scans
13.3 Linear Attention, RWKV, and RetNet
13.4 Neural ODEs, Latent ODEs, and ODE-RNNs
13.5 Neural CDEs and Irregularly-Sampled Data
13.6 Bridge: Unifying RNNs, SSMs, and Linear Attention

### Chapter 14. Deep Forecasting Architectures *(new)*
14.1 DeepAR and Probabilistic RNN Forecasting
14.2 N-BEATS and N-HiTS
14.3 Temporal Fusion Transformer (TFT)
14.4 Informer, Autoformer, and FEDformer
14.5 PatchTST, DLinear/NLinear, and the "Are Transformers Effective?" Debate
14.6 TSMixer, TiDE, and MLP-Based Forecasters

### Chapter 15. Temporal Foundation Models
15.1 Pretraining Paradigms for Time Series
15.2 Chronos, Lag-Llama, and MOMENT
15.3 TimeGPT, TimesFM, and Moirai
15.4 Tiny and Tabular Time-Series Models (TTM, TabPFN-TS)
15.5 LLMs for Time Series (LLMTime, Time-LLM, prompting and in-context forecasting)
15.6 Zero-Shot, Few-Shot, and Transfer; Future Directions

---

## Part IV. Temporal Representation Learning

### Chapter 16. Learning Temporal Representations
16.1 Representation Learning Fundamentals
16.2 Self-Supervised Pretext Tasks for Time Series
16.3 Contrastive Learning (TS2Vec, TF-C, and variants)
16.4 Masked Modeling for Time Series
16.5 Temporal Embeddings and Disentanglement

### Chapter 17. Generative Temporal Models
17.1 Autoencoders and Sequence Autoencoders
17.2 Variational Autoencoders and Sequential VAEs
17.3 GANs for Time Series (TimeGAN and beyond)
17.4 Diffusion Models for Time Series (TimeGrad, CSDI)
17.5 Synthetic Temporal Data Generation and Evaluation

### Chapter 18. Event and Sequence Modeling
18.1 Event Streams and Marked Sequences
18.2 Temporal Point Processes (Hawkes, neural TPPs)
18.3 Temporal and Dynamic Graphs
18.4 Event Prediction and Time-to-Event Modeling
18.5 Process Mining

---

## Part V. Uncertainty, Online, and Adaptive Learning

### Chapter 19. Probabilistic Forecasting and Uncertainty Quantification *(new)*
19.1 Point vs Probabilistic Forecasts
19.2 Proper Scoring Rules and Calibration
19.3 Quantile and Distributional Forecasting
19.4 Bayesian and Ensemble Approaches; Gaussian Processes for Time Series
19.5 Conformal Prediction for Time Series
19.6 Decision-Aware Evaluation of Forecasts

### Chapter 20. Online and Continual Learning
20.1 Streaming Data and Online Optimization
20.2 Concept Drift: Types and Detection
20.3 Online and Incremental Models
20.4 Continual and Lifelong Learning (catastrophic forgetting, replay, regularization)
20.5 Lifelong Temporal Systems

### Chapter 21. Adaptive Temporal AI Systems
21.1 Dynamic Model Updating and Retraining Triggers
21.2 Drift Detection in Production
21.3 Active Learning for Temporal Data
21.4 Human-in-the-Loop Adaptation

---

## Part VI. Sequential Decision Making

### Chapter 22. Markov Decision Processes
22.1 Sequential Decision Problems
22.2 The Markov Property
22.3 Policies, Value Functions, and Bellman Equations
22.4 Dynamic Programming (value/policy iteration)

### Chapter 23. Partial Observability and POMDPs *(new)*
23.1 Partial Observability and Belief States
23.2 Solving POMDPs (exact and approximate)
23.3 Recurrent and SSM-Based Agents for Partial Observability
23.4 Bridge: Filtering, Belief Tracking, and Memory

### Chapter 24. Bandits and Foundations of Reinforcement Learning
24.1 Multi-Armed Bandits
24.2 UCB, Thompson Sampling, and Regret
24.3 Contextual Bandits
24.4 Monte Carlo and Temporal-Difference Learning
24.5 Q-Learning and SARSA
24.6 Exploration vs Exploitation

### Chapter 25. Deep Reinforcement Learning
25.1 Deep Q-Networks and Variants
25.2 Policy Gradient Methods
25.3 Actor-Critic Methods (A2C/A3C, PPO, SAC)
25.4 Continuous Control
25.5 Practical Deep RL (stability, reproducibility, evaluation)

### Chapter 26. Advanced Reinforcement Learning
26.1 Model-Based RL
26.2 Offline RL
26.3 Multi-Agent RL
26.4 Safe and Constrained RL
26.5 Hierarchical RL and Temporal Abstraction (options)

### Chapter 27. Optimal Control and Imitation Learning *(new)*
27.1 LQR and the Linear-Quadratic-Gaussian Setting
27.2 Model Predictive Control (MPC)
27.3 Behavioral Cloning and DAgger
27.4 Inverse Reinforcement Learning and GAIL
27.5 Preference-Based RL and RLHF

### Chapter 28. Sequence Models for Decision Making *(new)*
28.1 RL as Sequence Modeling
28.2 Decision Transformer and Trajectory Transformer
28.3 Return-Conditioned and Goal-Conditioned Policies
28.4 Diffusion Planners (Diffuser, Decision Diffuser)
28.5 Bridge: Transformers/SSMs from Part III as Policies

### Chapter 29. World Models and Planning
29.1 Latent Environment Models
29.2 Dreamer and Recurrent World Models
29.3 Predictive State Representations
29.4 Planning in Latent Space (MuZero-style search)
29.5 Temporal Abstraction and Long-Horizon Planning

---

## Part VII. Building Intelligent Temporal Systems

### Chapter 30. Temporal Reasoning and Causality
30.1 Temporal Logic and Interval Reasoning
30.2 Causal Discovery for Time Series (Granger, PCMCI, causal nets)
30.3 Causal Effects and Treatment over Time
30.4 Counterfactual and What-If Analysis

### Chapter 31. Temporal AI Agents
31.1 Agent Architectures
31.2 Memory Systems (short/long-term, retrieval)
31.3 Planning and Tool Use
31.4 Long-Horizon Tasks and Credit Assignment
31.5 Agent Evaluation

### Chapter 32. Spatio-Temporal Intelligence
32.1 Mobility Modeling
32.2 Traffic Forecasting
32.3 Video Understanding
32.4 Activity Recognition
32.5 Dynamic and Spatio-Temporal Graph Learning

---

## Part VIII. Trustworthy and Deployed Temporal AI *(new part)*

### Chapter 33. Interpretability, Robustness, and Responsible Temporal AI *(new)*
33.1 Interpretability for Temporal Models (attention analysis, temporal saliency, SHAP for sequences)
33.2 Robustness and Adversarial Attacks on Time Series
33.3 Fairness and Bias in Temporal Predictions
33.4 Privacy and Federated Temporal Learning
33.5 Ethics, Governance, and Auditing

### Chapter 34. Deploying and Operating Temporal AI Systems *(new)*
34.1 Serving and Latency for Streaming Inference
34.2 Monitoring, Drift Alarms, and Retraining Loops (MLOps)
34.3 Feature/Online Stores and Data Contracts
34.4 Cost, Scaling, and Efficiency
34.5 Reliability, Versioning, and Incident Response

---

## Part IX. Applications and Future Directions

### Chapter 35. Industrial Applications
35.1 Finance (forecasting, volatility, risk, execution)
35.2 Healthcare (clinical time series, monitoring, prognosis)
35.3 Manufacturing and Predictive Maintenance
35.4 Energy and Climate
35.5 Autonomous Systems and Robotics
35.6 Scientific Discovery

### Chapter 36. Toward General Temporal Intelligence
36.1 Unified Sequence Models Across Modalities
36.2 Multimodal Temporal AI
36.3 Foundation Agents
36.4 Scaling Laws and Efficiency Frontiers
36.5 Open Challenges and Research Frontiers

> **Note.** Parts I–VII map onto a standard two-semester sequence; Part VIII
> (trustworthy/deployed) and Part IX (applications) can be taught as a project
> capstone or assigned as reading depending on course emphasis.

---

## Appendices

A. Mathematical Foundations and Unified Notation
B. Probability and Statistics Refresher
C. Optimization and Deep Learning Basics
D. PyTorch for Temporal AI (and JAX notes)
E. Datasets, Benchmarks, and Evaluation Protocols
F. Reproducibility, Compute, and Experiment Management
G. Solutions to Selected Exercises

---

## Change Log (v1 → v2)

**New chapters added**
- Frequency-Domain and Spectral Analysis (Ch.4)
- Multivariate and Econometric Models — VAR/GARCH/cointegration (Ch.6)
- State-Space and Continuous-Time Neural Models — S4/Mamba/Neural ODE (Ch.13)
- Deep Forecasting Architectures — DeepAR/TFT/N-BEATS/PatchTST (Ch.14)
- Probabilistic Forecasting and Uncertainty Quantification — conformal prediction (Ch.19)
- Partial Observability and POMDPs (Ch.23)
- Optimal Control and Imitation Learning (Ch.27)
- Sequence Models for Decision Making — Decision Transformer (Ch.28)
- Interpretability, Robustness, and Responsible Temporal AI (Ch.33)
- Deploying and Operating Temporal AI Systems / MLOps (Ch.34)

**Substantially expanded**
- Change-point detection folded into anomaly chapter (Ch.8)
- Bandits given full treatment with RL foundations (Ch.24)
- Foundation models updated to 2026 (TimesFM, Moirai, TTM, LLMs-for-TS) (Ch.15)
- Diffusion models for time series added to generative chapter (Ch.17)
- Causal discovery added to temporal reasoning (Ch.30)

**Cross-cutting additions**
- Per-chapter pedagogical scaffolding (objectives, exercises, case studies)
- Unified notation table (Appendix A)
- Three running datasets across chapters
- Explicit classical↔neural "bridge boxes"
- New Appendix F (reproducibility/compute)

**Structure:** 8 parts / 25 chapters → **9 parts / 36 chapters / 7 appendices**
