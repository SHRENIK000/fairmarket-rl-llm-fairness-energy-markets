from abc import ABC, abstractmethod

class AgentPolicy(ABC):
    """
    Abstract policy interface for an agent in the market.
    In the full implementation, each prosumer or consumer agent would use a policy (learned or otherwise) to decide on actions (bids/offers).
    """
    @abstractmethod
    def select_action(self, observation):
        """Choose an action given the current observation.
        For example, a prosumer might decide how much energy to sell and at what price.
        """
        raise NotImplementedError
