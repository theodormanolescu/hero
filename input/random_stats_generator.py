import random

from domain.character.stats_interface import StatsInterface


class RandomStatsGenerator(StatsInterface):

    def __init__(self):
        self.character_type = 'none'

    def set_type(self, character_type: str):
        self.character_type = character_type

    def get_health(self) -> int:
        if self.character_type == StatsInterface.HERO:
            return random.randint(70, 100)
        return random.randint(60, 90)

    def get_strength(self) -> int:
        if self.character_type == StatsInterface.HERO:
            return random.randint(70, 80)
        return random.randint(60, 90)

    def get_defence(self) -> int:
        if self.character_type == StatsInterface.HERO:
            return random.randint(45, 55)
        return random.randint(40, 60)

    def get_speed(self) -> int:
        if self.character_type == StatsInterface.HERO:
            return random.randint(40, 50)
        return random.randint(40, 60)

    def get_luck(self) -> int:
        if self.character_type == StatsInterface.HERO:
            return random.randint(10, 30)
        return random.randint(25, 40)

    def get_intelligence(self) -> int:
        if self.character_type == StatsInterface.HERO:
            return random.randint(30, 40)
        return random.randint(5, 10)
