from Application.EventInterface import EventInterface
from Domain.Character.Character import Character


class HeroCreated(EventInterface):
    def __init__(self, character: Character):
        self.character = character

    def get_name(self) -> str:
        return 'hero_created'
