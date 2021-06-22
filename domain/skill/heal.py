from domain.skill.skill import Skill


class Heal(Skill):
    NAME = 'heal'

    def __init__(self, value=20, cost=30, cooldown=0, hits=1):
        super().__init__(value, cost, cooldown, hits)

    def get_name(self) -> str:
        return Heal.NAME

    def process_value(self, character: 'Character'):
        """
        :type character: domain.character.character.Character
        """


