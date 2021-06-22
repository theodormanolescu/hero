from Application.EventInterface import EventInterface
from Domain.Character import Character
from Domain.Skill.Skill import Skill


class ReactedSkill(EventInterface):
    def __init__(self, character: Character, skill: Skill):
        self.character = character
        self.skill = skill

    def get_name(self) -> str:
        return 'reacted_skill'
