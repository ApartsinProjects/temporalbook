# Cross-Reference Map

Progressive-depth concepts that appear in multiple chapters at different levels, plus
the recurring "temporal thread" arcs where a classical idea returns in learned form.
The Cross-Reference Architect (Agent #13) uses this map to insert inline hyperlinks
(at least 3 cross-chapter links per section). Paths follow the relative-path rules in
`BOOK_CONFIG.md`.

## The Temporal Thread (classical -> learned arcs)

Each arc is a deliberate callback. When writing the later chapter, link back to the
earlier one with a "Looking Back" callout; when writing the earlier chapter, foreshadow
with a "Thesis Thread" callout.

| Arc | Introduced (classical) | Returns (learned) | Returns again (frontier) |
|-----|------------------------|-------------------|--------------------------|
| Recursive state estimation | Kalman filter (Ch 7) | RNN as learned filter (Ch 10) | Structured SSM: S4/Mamba (Ch 13) |
| Latent discrete state | HMM (Ch 7) | Sequential VAE (Ch 17) | Belief-state POMDP agent (Ch 23) |
| Linear autoregression | AR/ARIMA (Ch 5) | Linear attention / SSM recurrence (Ch 13) | In-context forecasting (Ch 15) |
| Frequency decomposition | Fourier/wavelets (Ch 4) | Frequency-domain forecasters: Autoformer/FEDformer (Ch 14) | Spectral mixers in foundation models (Ch 15) |
| Multivariate dependence | VAR / Granger (Ch 6) | Temporal/dynamic graphs (Ch 18) | Spatio-temporal GNNs (Ch 32) |
| Volatility / heteroskedasticity | GARCH (Ch 6) | Probabilistic forecasting heads: DeepAR (Ch 14) | Conformal prediction intervals (Ch 19) |
| Denoising | Exponential smoothing / restoration (Ch 5, Ch 8) | Diffusion for time series: CSDI/TimeGrad (Ch 17) | Diffusion planners (Ch 28) |
| Sequential decision | MDP / dynamic programming (Ch 22) | Deep RL: DQN/PPO (Ch 25) | RL as sequence modeling: Decision Transformer (Ch 28) |
| Partial observability | Particle filter / belief (Ch 7) | POMDP (Ch 23) | Recurrent/SSM world-model agents (Ch 29) |
| Planning with a model | Optimal control / MPC (Ch 27) | Model-based RL (Ch 26) | Learned world models: Dreamer/MuZero (Ch 29) |

## Progressive-Depth Concepts (appear at increasing depth)

- **Attention / self-attention**: introduced (Ch 12), efficient/long-sequence variants (Ch 12.5, Ch 13), as forecaster (Ch 14: TFT, PatchTST, Informer), in foundation models (Ch 15), as policy (Ch 28).
- **Stationarity & distribution shift**: defined (Ch 3.2), violated and tested (Ch 6 cointegration), concept drift (Ch 20.2), drift in production (Ch 21.2, Ch 34.2), robustness (Ch 33.2).
- **Uncertainty quantification**: error bars first appear (Ch 5 diagnostics), full treatment (Ch 19), Bayesian filtering (Ch 7), RL exploration uncertainty (Ch 24.6), decision-aware evaluation (Ch 19.6).
- **Evaluation & leakage**: protocols (Ch 2.6), forecasting metrics and backtesting (Ch 5.7, Ch 19), RL evaluation (Ch 25.5), benchmarks appendix (Appendix E).
- **Representation learning**: embeddings (Ch 16), self-supervised pretext (Ch 16.2), masked modeling underpins foundation models (Ch 15.1), event embeddings (Ch 18).
- **Markov property**: random processes (Ch 3.1), HMM (Ch 7.5), MDP (Ch 22.2), POMDP relaxation (Ch 23).
- **Backpropagation through time**: introduced (Ch 9.3), RNN training (Ch 10), truncation and stability (Ch 10.6), credit assignment in agents (Ch 31.4).

## Forward Pointers from Foundations

- Ch 1 (Introduction) previews every part; it should link forward to at least one anchor chapter per part.
- Ch 2 (Data Engineering) leakage rules are referenced by every forecasting and evaluation section.
- Appendix A (Unified Notation) is linked the first time each major symbol appears.

## Application Callbacks

The three running datasets (finance, healthcare, sensor/IoT; see BOOK_CONFIG.md) create
cross-links: any chapter using a dataset links back to where it was introduced and
forward to its appearance in Ch 35 (Industrial Applications).
