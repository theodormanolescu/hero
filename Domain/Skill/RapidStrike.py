from Domain.Skill.Skill import Skill


class RapidStrike(Skill):
    NAME = 'rapid_strike'

    def __init__(self, modifier: int):
        super().__init__(modifier, hits=2)

    def process_value(self, defence: int) -> int:
        return self.value - defence
