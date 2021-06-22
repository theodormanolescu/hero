from application.event_dispatcher import EventDispatcher
from domain.character.character import Character
from domain.character.repository import CharacterRepository
from domain.character.stats_interface import StatsInterface
from domain.skill.repository import SkillRepository


class CharacterCreation:
    def __init__(self, stats: StatsInterface,
                 character_repository: CharacterRepository,
                 skill_repository: SkillRepository, dispatcher: EventDispatcher):
        self.stats = stats
        self.character_repository = character_repository
        self.skill_repository = skill_repository
        self.dispatcher = dispatcher

    def new_hero(self) -> Character:
        self.stats.set_type(StatsInterface.HERO)
        hero = Character(
            self.dispatcher,
            health=self.stats.get_health(),
            resource=self.stats.get_intelligence() * self.character_repository.get_resource_multiplier(),
            strength=self.stats.get_strength(),
            defence=self.stats.get_defence(),
            speed=self.stats.get_speed(),
            luck=self.stats.get_luck(),
            character_type=StatsInterface.HERO
        )

        for skill in self.skill_repository.get_skills_for_character(hero):
            hero.add_skill(skill.NAME, skill)

        return hero

    def new_enemy(self) -> Character:
        enemy = Character(
            self.dispatcher,
            health=self.stats.get_health(),
            resource=self.stats.get_intelligence() * self.character_repository.get_resource_multiplier(),
            strength=self.stats.get_strength(),
            defence=self.stats.get_defence(),
            speed=self.stats.get_speed(),
            luck=self.stats.get_luck()
        )

        for skill in self.skill_repository.get_skills_for_character(enemy):
            enemy.add_skill(skill.NAME, skill)

        return enemy
