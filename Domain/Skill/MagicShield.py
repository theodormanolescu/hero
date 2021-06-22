from Domain.Skill.Skill import Skill


class MagicShield(Skill):
    NAME = 'magic_shield'

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return MagicShield.NAME

    def process_value(self, damage: int) -> int:
        return round(damage/2) if damage > 0 else damage
