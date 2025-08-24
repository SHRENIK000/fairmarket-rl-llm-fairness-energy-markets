import os
import argparse
import yaml

from fairmarket_rl.demo.demo_env import ToyMarketEnv
from fairmarket_rl.demo.random_policy import RandomPolicy

def main():
    parser = argparse.ArgumentParser(description="Run FairMarket-RL toy demo")
    parser.add_argument("--config", "-c", type=str, default="configs/demo.yaml",
                        help="Path to the YAML configuration file for the demo.")
    args = parser.parse_args()
    config_path = args.config
    # Load configuration
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load config file {config_path}: {e}")
    # Set random seed if provided (for reproducibility)
    seed = None
    if "random_seed" in config:
        seed = config["random_seed"]
        try:
            import random
            random.seed(seed)
        except Exception as e:
            print(f"Warning: Could not set random seed due to {e}")
    # Configure the toy environment parameters
    env_cfg = config.get("environment", {})
    num_prosumers = env_cfg.get("n_prosumers", env_cfg.get("num_prosumers", 1))
    num_consumers = env_cfg.get("n_consumers", env_cfg.get("num_consumers", 1))
    # total steps can be specified directly or via days*slots_per_day
    if "days" in env_cfg and "slots_per_day" in env_cfg:
        steps = env_cfg["days"] * env_cfg["slots_per_day"]
    else:
        steps = env_cfg.get("steps", 24)
    max_supply = env_cfg.get("max_supply_kwh", 5.0)
    max_demand = env_cfg.get("max_demand_kwh", 5.0)
    # Initialize environment and random policy
    env = ToyMarketEnv(num_prosumers, num_consumers, max_supply=max_supply, max_demand=max_demand, steps=steps)
    policy = RandomPolicy(max_supply=max_supply, max_demand=max_demand)
    # Prepare results directory
    os.makedirs("results", exist_ok=True)
    output_file = os.path.join("results", "demo_run.csv")
    # Run simulation
    obs = env.reset()
    done = False
    step_counter = 0
    # Open CSV file for writing results
    with open(output_file, "w") as f:
        # Write header
        f.write("step,FTG,FBS,FPP\n")
        while not done and step_counter < steps:
            # For each step, generate actions for each agent using the random policy
            # (In this simple demo, the ToyMarketEnv itself does not actually use these actions,
            # but we'll demonstrate the interface.)
            for _ in range(num_prosumers):
                _ = policy.act_for_prosumer()
            for _ in range(num_consumers):
                _ = policy.act_for_consumer()
            # Advance environment by one step
            obs, done = env.step()
            metrics = env.get_last_metrics()
            # Write metrics to CSV
            f.write(f"{step_counter},{metrics.get('FTG', '')},{metrics.get('FBS', '')},{metrics.get('FPP', '')}\n")
            step_counter += 1
    print(f"Toy demo finished. Results saved to {output_file}")

if __name__ == "__main__":
    main()
