import random
from fairmarket_rl.api.environment import P2PMarketEnv

class ToyMarketEnv(P2PMarketEnv):
    """
    A toy environment for demonstration purposes.
    Simulates a very simplified P2P energy market with a few agents using random values.
    This does NOT represent the real environment logic.
    """
    def __init__(self, num_prosumers=1, num_consumers=1, max_supply=5.0, max_demand=5.0, steps=24):
        """
        Initialize the toy environment.
        :param num_prosumers: Number of prosumer agents (sellers).
        :param num_consumers: Number of consumer agents (buyers).
        :param max_supply: Maximum energy a prosumer can supply in a time step (kWh).
        :param max_demand: Maximum energy a consumer can demand in a time step (kWh).
        :param steps: Total number of steps (auction slots) in the simulation.
        """
        self.num_prosumers = num_prosumers
        self.num_consumers = num_consumers
        self.max_supply = max_supply
        self.max_demand = max_demand
        self.total_steps = steps
        self.current_step = 0
        # State placeholders (not used in a meaningful way for this toy example)
        self.last_metrics = None

    def reset(self):
        """Reset the toy environment to the beginning."""
        self.current_step = 0
        self.last_metrics = None
        # No meaningful observation to return in this toy env; return a placeholder (e.g., step 0).
        return {"step": 0}

    def step(self, actions=None):
        """
        Simulate one time step (one market slot).
        :param actions: (Optional) actions for each agent. In this toy env, actions can be ignored,
                        as we generate random trades.
        :return: observation for next step, done flag
        """
        if self.current_step >= self.total_steps:
            # If already at end, do nothing
            return None, True
        # Generate random supply for each prosumer and random demand for each consumer
        supplies = [random.uniform(0, self.max_supply) for _ in range(self.num_prosumers)]
        demands = [random.uniform(0, self.max_demand) for _ in range(self.num_consumers)]
        total_supply = sum(supplies)
        total_demand = sum(demands)
        # Determine peer-to-peer traded energy and grid usage
        p2p_traded = min(total_supply, total_demand)
        # If supply exceeds demand, surplus goes unsold (or to grid export); if demand exceeds supply, deficit is met by grid.
        grid_usage = total_demand - p2p_traded if total_demand > p2p_traded else 0.0
        # Compute fairness metrics (FTG, FBS, FPP) in a trivial way
        if total_demand > 1e-9:
            FTG = p2p_traded / total_demand  # fraction of demand met by P2P
        else:
            # If no demand, define FTG as 1 (no grid needed)
            FTG = 1.0
        # Fairness between sellers (FBS): if multiple prosumers, measure how evenly they shared the P2P trade.
        FBS = 1.0
        if p2p_traded > 1e-9 and self.num_prosumers > 1:
            # Calculate each prosumer's contribution to P2P trade
            sold = []
            for s in supplies:
                # allocate trade proportionally to supply
                sold.append(p2p_traded * (s / total_supply) if total_supply > 0 else 0.0)
            if any(q > 1e-9 for q in sold):
                # consider only prosumers who sold > 0
                shares = [q / p2p_traded for q in sold if q > 1e-9]
                if shares:
                    max_share = max(shares)
                    min_share = min(shares)
                    FBS = max(0.0, 1.0 - (max_share - min_share))
        # Fairness of pricing (FPP): in the toy model, assume all P2P trades happen at one price,
        # so the only price disparity is if grid is involved.
        FPP = 1.0
        if p2p_traded > 1e-9 and grid_usage > 1e-9:
            # If both P2P and grid trades occurred, there was a price difference between local and grid transactions.
            FPP = 0.9  # arbitrarily represent some spread
        # If no P2P trades or no grid usage, FPP remains 1.0 (no price spread or single source).
        # Record metrics for this step
        self.last_metrics = {"FTG": round(FTG, 3), "FBS": round(FBS, 3), "FPP": round(FPP, 3)}
        # Increment step counter
        self.current_step += 1
        done = (self.current_step >= self.total_steps)
        # Next observation can simply include the step number
        next_obs = {"step": self.current_step}
        return next_obs, done

    def get_last_metrics(self):
        """Get the metrics (FTG, FBS, FPP) from the last executed step."""
        return self.last_metrics if self.last_metrics is not None else {}
