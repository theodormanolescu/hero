from domain.skill.skill import Skill


class BasicAttack(Skill):
    NAME = 'basic_attack'

    def __init__(self, modifier: int):
        super().__init__(modifier)

    def get_name(self) -> str:
        return BasicAttack.NAME

    def process_value(self, defence: int) -> int:
        return self.value - defence
