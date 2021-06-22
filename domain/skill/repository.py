from abc import abstractmethod

from domain.character.character import Character
from domain.skill.skill import Skill


class SkillRepository:
    @abstractmethod
    def get_skills_for_character(self, character: Character) -> [Skill]:
        pass
