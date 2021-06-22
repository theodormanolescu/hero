from Domain.Skill.Skill import Skill


class BasicAttack(Skill):
    NAME = 'basic_attack'

    def __init__(self, modifier: int):
        super().__init__(modifier)

    def process_value(self, defence: int) -> int:
        return self.value - defence