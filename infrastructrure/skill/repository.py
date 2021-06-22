from domain.character.character import Character
from domain.character.stats_interface import StatsInterface
from domain.skill.basic_attack import BasicAttack
from domain.skill.magic_shield import MagicShield
from domain.skill.no_reaction import NoReaction
from domain.skill.rapid_strike import RapidStrike
from domain.skill.repository import SkillRepository
from domain.skill.skill import Skill


class InMemorySkillRepository(SkillRepository):
    def get_skills_for_character(self, character: Character) -> [Skill]:
        skills = []
        if character.character_type == StatsInterface.HERO:
            skills.append(RapidStrike(character.strength))
            skills.append(MagicShield())
        skills.append(BasicAttack(character.strength))
        skills.append(NoReaction())

        return skills
