from Domain.Character.TookDamage import TookDamage
from Domain.Fight.FightEnded import FightEnded
from Domain.Game.EnemyCreated import EnemyCreated
from Domain.Game.GameEnded import GameEnded
from Domain.Game.GameStarted import GameStarted
from Domain.Game.HeroCreated import HeroCreated
from Domain.Skill.ReactedSkill import ReactedSkill
from Domain.Skill.SkillUsed import SkillUsed


class GameListener:
    def game_started(self, event: GameStarted):
        print(f"New game started with {event.difficulty_level} difficulty")

    def hero_created(self, event: HeroCreated):
        print(f"""
        New hero was created with:
            {event.character.strength} strength,
            {event.character.defence} defence,
            {event.character.resource} mana,
            {event.character.speed} speed,
            {event.character.health} health,
            {event.character.luck} luck
        """)

    def enemy_created(self, event: EnemyCreated):
        print(f"""
        New enemy was created with:
            {event.character.strength} strength,
            {event.character.defence} defence,
            {event.character.resource} mana,
            {event.character.speed} speed,
            {event.character.health} health,
            {event.character.luck} luck
        """)

    def game_ended(self, event: GameEnded):
        print(f"""
        The game has ended.
        Our hero had {event.fights} fights
        And lasted {event.rounds} rounds in the last fight
        """)

    def fight_ended(self, event: FightEnded):
        fighter = list(filter(lambda character: character.alive, event.fighters)).pop()
        print(f"""
        The fight has ended.
        {fighter.character_type} won the fight
        """)

    def skill_used(self, event: SkillUsed):
        print(f"""
        The {event.attacker.character_type} used {event.skill.NAME} on {event.defender.character_type}
        """)

    def took_damage(self, event: TookDamage):
        print(f"""
        The {event.character.character_type} took {event.value} damage
        """)

    def reacted_skill(self, event: ReactedSkill):
        print(f"""
        The {event.character.character_type} reacted with {event.skill.NAME} 
        """)