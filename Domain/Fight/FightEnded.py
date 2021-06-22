from typing import List

from Application.EventInterface import EventInterface
from Domain.Character.Character import Character


class FightEnded(EventInterface):
    def __init__(self, fighters: List[Character]):
        self.fighters = fighters

    def get_name(self) -> str:
        return 'fight_ended'
