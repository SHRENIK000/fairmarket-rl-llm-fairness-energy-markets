from abc import ABC, abstractmethod

class P2PMarketEnv(ABC):
    """
    Abstract interface for the peer-to-peer energy market environment.
    In the full FairMarket-RL system, this environment handles multiple agents (prosumers and consumers),
    runs a continuous double auction for each time slot, and computes economic rewards plus fairness metrics.
    """
    @abstractmethod
    def reset(self):
        """Initialize the environment state and return the initial observation(s).
        In the full implementation, this would typically generate a new episode (e.g., new day(s) of trading).
        """
        raise NotImplementedError

    @abstractmethod
    def step(self, actions):
        """Execute one time step of the environment using the given agent action(s).
        In the full implementation, `actions` would include all agents' bids/offers for the current auction slot.
        Returns observations for the next time step, as well as any metrics or rewards.
        """
        raise NotImplementedError

    # The full environment may include additional methods for retrieving results, metrics, etc.
    # Those are omitted here for brevity.
