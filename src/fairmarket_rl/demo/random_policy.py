import random

class RandomPolicy:
    """
    A simple random policy for demonstration. This policy ignores observations and returns random actions.
    In a real scenario, this might represent an agent's strategy (learned or heuristic).
    """
    def __init__(self, max_supply=5.0, max_demand=5.0):
        self.max_supply = max_supply
        self.max_demand = max_demand

    def act_for_prosumer(self, observation=None):
        """Return a random supply quantity (kWh) for a prosumer."""
        return random.uniform(0, self.max_supply)

    def act_for_consumer(self, observation=None):
        """Return a random demand quantity (kWh) for a consumer."""
        return random.uniform(0, self.max_demand)
