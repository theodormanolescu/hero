from abc import abstractmethod

from Domain.Character.Character import Character
from Domain.Skill.Skill import Skill


class SkillRepository:
    @abstractmethod
    def get_skills_for_character(self, character: Character) -> [Skill]:
        pass
