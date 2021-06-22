from application.event_interface import EventInterface


class HeroCreated(EventInterface):
    def __init__(self, character: 'Character'):
        self.character = character

    def get_name(self) -> str:
        return 'hero_created'
