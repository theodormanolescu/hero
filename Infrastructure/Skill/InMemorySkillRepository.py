from Domain.Character.Character import Character
from Domain.Character.StatsInterface import StatsInterface
from Domain.Skill.BasicAttack import BasicAttack
from Domain.Skill.MagicShield import MagicShield
from Domain.Skill.NoReaction import NoReaction
from Domain.Skill.RapidStrike import RapidStrike
from Domain.Skill.SkillRepository import SkillRepository


class InMemorySkillRepository(SkillRepository):
    def get_skills_for_character(self, character: Character) -> []:
        skills = []
        if character.character_type == StatsInterface.HERO:
            skills.append(RapidStrike(character.strength))
            skills.append(MagicShield())
        skills.append(BasicAttack(character.strength))
        skills.append(NoReaction())

        return skills
