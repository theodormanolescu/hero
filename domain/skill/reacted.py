from application.event_interface import EventInterface
from domain.skill.skill import Skill


class Reacted(EventInterface):
    def __init__(self, character: 'Character', skill: Skill):
        self.character = character
        self.skill = skill

    def get_name(self) -> str:
        return 'reacted_skill'
