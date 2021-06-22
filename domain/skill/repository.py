from domain.character.character import Character
from domain.skill.skill import Skill


class SkillRepository:
    def get_skills_for_character(self, character: Character) -> [Skill]:
        raise NotImplemented()
