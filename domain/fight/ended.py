from typing import List

from application.event_interface import EventInterface


class Ended(EventInterface):
    def __init__(self, fighters: List['Character']):
        """

        :type fighters: [domain.character.character.Character]
        """
        self.fighters = fighters

    def get_name(self) -> str:
        return 'fight_ended'
