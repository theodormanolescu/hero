import random

from domain.character.action_interface import ActionInterface
from domain.character.character import Character
from domain.character.stats_interface import StatsInterface
from domain.skill.basic_attack import BasicAttack
from domain.skill.heal import Heal
from domain.skill.magic_shield import MagicShield
from domain.skill.no_reaction import NoReaction
from domain.skill.rapid_strike import RapidStrike


class RandomActionGenerator(ActionInterface):
    def take_action(self, character: Character) -> str:
        if character.character_type == StatsInterface.HERO and RandomActionGenerator.has_chance(10):
            return RapidStrike.NAME
        return BasicAttack.NAME

    def react(self, character: Character):
        if character.character_type == StatsInterface.HERO and RandomActionGenerator.has_chance(20):
            return MagicShield.NAME
        return NoReaction.NAME

    def rest(self) -> str:
        return Heal.NAME

    @staticmethod
    def has_chance(value):
        return random.randrange(0, 100) <= value
