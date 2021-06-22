import random

from Domain.Character.ActionInterface import ActionInterface
from Domain.Character.Character import Character
from Domain.Character.StatsInterface import StatsInterface
from Domain.Skill.BasicAttack import BasicAttack
from Domain.Skill.MagicShield import MagicShield
from Domain.Skill.NoReaction import NoReaction
from Domain.Skill.RapidStrike import RapidStrike


class RandomActionGenerator(ActionInterface):
    def take_action(self, character: Character) -> str:
        if character.character_type == StatsInterface.HERO and RandomActionGenerator.has_chance(10):
            return RapidStrike.NAME
        return BasicAttack.NAME

    def react(self, character: Character):
        if character.character_type == StatsInterface.HERO and RandomActionGenerator.has_chance(60):
            return MagicShield.NAME
        return NoReaction.NAME

    @staticmethod
    def has_chance(value):
        return random.randrange(0, 100) <= value
