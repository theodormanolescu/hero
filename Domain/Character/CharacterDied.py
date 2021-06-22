from Application.EventInterface import EventInterface
from Domain.Character import Character


class CharacterDied(EventInterface):
    def __init__(self, character: Character):
        self.character = character

    def get_name(self) -> str:
        return 'character_died'
