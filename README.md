# FairMarket-RL (Public Release)

FairMarket-RL is a multi-agent reinforcement learning framework for peer-to-peer (P2P) electricity markets that integrates **fairness shaping** via large language model (LLM) feedback. It enables prosumers (households with solar PV) and consumers to trade energy locally in a continuous double auction while receiving real-time fairness guidance (e.g. discouraging over-reliance on the grid, ensuring equitable market participation, and fair pricing). This public repository provides the high-level interface, configuration schema, and a small **toy demo** of FairMarket-RL for educational and reference purposes. **The core training algorithms, market simulator, and fairness logic are withheld** as this is an ongoing research project.

**Papers in the FairMarket-RL series**
1. [FairMarket-RL: LLM-Guided Fairness Shaping for Multi-Agent Reinforcement Learning in Peer-to-Peer Markets](https://arxiv.org/abs/2506.22708)

2. Scalable Fairness Shaping with LLM-Guided Multi-Agent Reinforcement Learning for Peer-to-Peer Electricity Markets

## What's Included vs. What's Withheld
**Included in this public repo:**
- **Interface Definitions:** Abstract classes and method signatures reflecting the key components of FairMarket-RL (environment, agents, etc.), allowing users to see how the system is structured without revealing internal logic.
- **Toy Example Environment:** A simplified `ToyMarketEnv` with a couple of agents and random trading behavior, to demonstrate how the interface works. This does *not* reflect the real market simulation.
- **Configuration Schema:** A sample YAML config (`configs/demo.yaml`) that mirrors the structure of the real configuration (agents, environment, etc.), but with safe, toy values.
- **CLI Script:** A command-line interface (`fairmarket_rl/cli.py`) to run the toy demo, producing a small synthetic log in `results/`. This shows how one would use the interfaces.
- **Documentation & Metadata:** README, license, citation info, and guidelines for contributions, security, and how to request full access.

**Withheld (not included publicly):**
- **Full Market Simulator:** The detailed environment that implements the continuous double auction, realistic load/PV profiles, battery storage dynamics, and grid settlement is kept private. (Replaced here by a stub `ToyMarketEnv` with minimal logic.)
- **Training and RL Algorithms:** The reinforcement learning training loop (e.g. Proximal Policy Optimization and the fairness-shaped reward computations) and optimization code are not included. (In the demo, agents use a random policy instead of learning.)
- **LLM Fairness Critic:** The integration with an LLM (large language model) that provides fairness scores (FTG, FBS, FPP) from market outcomes is omitted. In this public version, fairness metrics are either static or randomly generated for demonstration.
- **Real Data & Configs:** Actual experimental scenarios, real community dataset, and extensive hyperparameter configurations used in the paper are not provided. The demo uses synthetic data and trivial parameters to avoid revealing proprietary data or tuned values.
- **Evaluation & Results Code:** Scripts for extensive evaluation, plotting, and the generation of results/figures in the paper are withheld. Only basic logging to CSV is demonstrated publicly.

We have taken care to ensure that *no sensitive or proprietary information (such as API keys, real data, or institutional details) is present* in this repository. If you find something we missed, please let us know or open an issue.

## Quickstart
**Requirements:** Python 3.8+ (no external dependencies beyond the standard library and PyYAML for config parsing). You do *not* need GPUs or any special ML frameworks to run the toy demo.

1. **Install the package (editable mode recommended for development):**
   ```bash
   git clone https://github.com/{{YOUR_GITHUB_HANDLE_OR_ORG}}/fairmarket-rl-public.git
   cd fairmarket-rl-public
   pip install -e .
   ```
2. **Run the toy demo:**
   ```bash
   python -m fairmarket_rl.cli --config configs/demo.yaml
   ```
   This will simulate a few trading steps in a toy P2P market and write a small log file (e.g. `results/demo_run.csv`). The log will contain some fairness metrics (FTG, FBS, FPP) for each step with **synthetic values**.
3. **Check the output:** After running, open the CSV in `results/` to see the recorded metrics per time step. For example:
   ```text
   step,FTG,FBS,FPP
   0,0.00,1.0,1.0
   1,0.50,1.0,0.9
   2,1.00,1.0,1.0
   ... 
   ```
   (These values are illustrative. In the demo, FTG will vary between 0 and 1 depending on random grid vs. peer usage; FBS and FPP are fixed at 1.0 in the one-prosumer scenario.)

4. You can modify `configs/demo.yaml` to adjust the number of agents or steps in the toy simulation. Note that this will not reproduce results from the paper, as the core logic is absent.

## Active Research Disclaimer
This code is a **research prototype** and **not a full production implementation**. It is provided for transparency and educational purposes regarding the structure of our solution. The public code cannot train or run the actual FairMarket-RL algorithm due to the withheld components. We welcome feedback and questions, but please understand that features are limited by design.

## Citing this Work
If you use the ideas or interface from FairMarket-RL in your research, please cite our paper:

*Shrenik Jadhav, Birva Sevak, Srijita Das, Akhtar Hussain, Wencong Su, Van-Hai Bui. "Scalable Fairness Shaping with LLM-Guided Multi-Agent Reinforcement Learning for Peer-to-Peer Electricity Markets." 2025.* 

BibTeX and citation metadata are provided in [CITATION.cff](CITATION.cff).

## Requesting Full Access
Qualified researchers can request access to the full private repository (which includes the training code, full environment, and data) by following the instructions in [REQUEST_FULL_ACCESS.md](REQUEST_FULL_ACCESS.md). We typically require signing an NDA or similar agreement for non-commercial research use.

## License
This repository is released under the MIT License (see [LICENSE](LICENSE)). Note that the full FairMarket-RL code may be under different terms for those who obtain access.

## Contact
For questions or inquiries, please contact the authors via email (see REQUEST_FULL_ACCESS.md for contact info). You can also open an issue on this public repo for general questions.
