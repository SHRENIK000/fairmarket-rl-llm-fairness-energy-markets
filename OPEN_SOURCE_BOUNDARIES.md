**Open-Source Release Boundaries for FairMarket-RL**

This memo outlines which components of FairMarket-RL have been made public and which remain closed-source, along with the rationale for these decisions. The goal is to balance transparency with protection of ongoing research innovations and sensitive assets.

**Publicly Released (Open):** The public repository contains the high-level *interface* of the FairMarket-RL framework and a minimal demo:
- Abstract class definitions (interfaces) for the environment and agent policies, showing the structure and function signatures used in FairMarket-RL.
- A lightweight toy environment and random policy implementation that demonstrate how the system might be used, without including any of the complex logic or learned decision-making.
- Configuration files and documentation that mirror the terminology and overall design of the system (e.g., fairness metrics names, config keys for numbers of agents, etc.), allowing others to understand the scope and setup of FairMarket-RL.
- All general documentation, including README, licensing, citation info, and guidelines, to contextualize the project and explain how to get access to the full system.
Importantly, **the public code is safe and self-contained**: it has no proprietary data or secrets, and its outputs are synthetic (random or fixed values) so as not to reveal any insights about the withheld algorithms or data.

**Withheld (Closed-Source) Components:** The following key components are **not** included in the public release:
- **Full Market Environment & Simulator:** The core simulation that implements the continuous double auction, realistic prosumer/consumer behavior, grid interactions, and battery storage dynamics is kept private. This is a significant part of our research contribution and includes domain-specific innovations that are under active study.
- **Fairness Shaping & LLM Critic Integration:** The mechanism by which an LLM evaluates trades and provides fairness scores (FTG, FBS, FPP) in real time, and how those scores shape agent rewards, is not open-sourced. This component not only relies on an external API (OpenAI GPT) and associated credentials, but also encapsulates novel techniques that are pending publication and/or intellectual property review.
- **Reinforcement Learning Training Code:** The implementation of the multi-agent RL algorithm (e.g., PPO with curriculum learning for fairness) and the neural network models for agent policies are withheld. Releasing this could enable replication of our results without proper collaboration and might expose methods that are still being refined for potential future publications.
- **Experimental Configurations & Data:** The exact configurations used in our experiments (such as hyperparameters for 10,000 training episodes, scaling factors for fairness, etc.), as well as the real-world dataset of energy profiles, are not included. The dataset may have usage restrictions and the specific configurations are considered part of the "secret sauce" that led to our reported results. Excluding these prevents unintended use of proprietary data and preserves the competitive advantage of our research.
- **Evaluation & Plotting Scripts:** Any scripts used to evaluate trained models, perform sensitivity analyses, or generate figures for the paper are not part of the public release. These often contain hard-coded references to data and assumptions from the full environment.
- **Credentials/Secrets:** All API keys (for LLM services) and any other secret tokens have been removed. Their presence is neither needed nor appropriate in a public repo.

**Rationale for Withholding:** The withheld components contain the core intellectual contributions of FairMarket-RL and/or rely on resources that cannot be openly shared. By keeping these private, we:
  - Protect the ongoing research and potential future commercialization or academic novelty. Prematurely open-sourcing the full code could undermine publication opportunities or patent filings related to our fairness shaping approach.
  - Avoid misuse or misinterpretation of an incomplete system. Releasing the code without certain data or context could lead to attempts to reproduce results incorrectly, which might harm the project's reputation or mislead others.
  - Comply with any licensing or ethical constraints (for example, the real energy dataset might be under a license that forbids open redistribution; the OpenAI API usage has cost and terms associated).
  - Maintain control over how and with whom the full system is shared. We prefer to collaborate or share under agreements (e.g., NDAs) to ensure proper use and attribution.

**Access for Researchers:** We are committed to transparency and scientific collaboration. Researchers who have a legitimate need for the full FairMarket-RL code (e.g., to reproduce results or extend the work) can request access by contacting us and agreeing to terms of use (see `REQUEST_FULL_ACCESS.md`). Each request will be evaluated to balance openness with the considerations above.

**In Summary:** The public repository provides a **useful glimpse** into FairMarket-RL’s structure and an **educational demo**, but it deliberately omits the complex algorithms, data, and configurations that drive the actual results reported in our paper. This approach ensures we can share knowledge and receive feedback on the framework’s design, while safeguarding the essential components until we deem it appropriate to release them (for example, after further validation, publication, or formal agreements). We believe this strategy serves both the open-source community’s interests and our research team’s responsibilities.
________________________________________
