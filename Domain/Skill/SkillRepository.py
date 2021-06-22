from abc import abstractmethod

from Domain.Character.Character import Character


class SkillRepository:
    @abstractmethod
    def get_skills_for_character(self, character: Character) -> {}:
        pass
