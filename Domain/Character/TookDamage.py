from Application.EventInterface import EventInterface
from Domain.Character.Character import Character


class TookDamage(EventInterface):
    def __init__(self, character: Character, value: int):
        self.character = character
        self.value = value

    def get_name(self) -> str:
        return 'took_damage'
