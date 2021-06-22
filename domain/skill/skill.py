class Skill:
    def __init__(self, value=0, cost=0, cooldown=0, hits=1):
        self.value = value
        self.cost = cost
        self.cooldown = cooldown
        self.hits = hits

    def get_name(self) -> str:
        raise NotImplemented()

    def process_value(self, *args):
        raise NotImplemented()
