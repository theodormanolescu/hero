from abc import abstractmethod


class Skill:
    def __init__(self, value=0, cost=0, cooldown=0, hits=1):
        self.value = value
        self.cost = cost
        self.cooldown = cooldown
        self.hits = hits

    @abstractmethod
    def process_value(self, **kwargs):
        pass
