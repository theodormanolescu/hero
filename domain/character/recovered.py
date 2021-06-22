from application.event_interface import EventInterface


class Recovered(EventInterface):
    def __init__(self, character: 'Character', value: int):
        """
        :type character: domain.character.character.Character
        """
        self.character = character
        self.value = value

    def get_name(self) -> str:
        return 'character_recovered'
