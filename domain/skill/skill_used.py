from application.event_interface import EventInterface
from domain.skill.skill import Skill


class SkillUsed(EventInterface):
    def __init__(self, attacker: 'Character', defender: 'Character', skill: Skill):
        self.attacker = attacker
        self.defender = defender
        self.skill = skill

    def get_name(self) -> str:
        return 'skill_used'
