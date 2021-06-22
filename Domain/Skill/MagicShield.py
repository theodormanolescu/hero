from Domain.Skill.Skill import Skill


class MagicShield(Skill):
    NAME = 'magic_shield'

    def __init__(self):
        super().__init__()

    def process_value(self, modifier: int) -> int:
        if modifier > 0:
            modifier = modifier / 2
        return modifier
