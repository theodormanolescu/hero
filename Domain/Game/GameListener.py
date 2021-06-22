from Domain.Character.CharacterDied import CharacterDied
from Domain.Character.TookDamage import TookDamage
from Domain.Fight.FightEnded import FightEnded
from Domain.Game.EnemyCreated import EnemyCreated
from Domain.Game.GameEnded import GameEnded
from Domain.Game.GameStarted import GameStarted
from Domain.Game.HeroCreated import HeroCreated
from Domain.Skill.ReactedSkill import ReactedSkill
from Domain.Skill.SkillUsed import SkillUsed


class GameListener:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    WHITE = '\033[0m'

    @staticmethod
    def game_started(event: GameStarted) -> None:
        print(f"New game started with {event.difficulty_level} difficulty")

    @staticmethod
    def hero_created(event: HeroCreated) -> None:
        print(GameListener.GREEN + f"""
        New hero was created with:
            {event.character.strength} strength,
            {event.character.defence} defence,
            {event.character.resource} mana,
            {event.character.speed} speed,
            {event.character.health} health,
            {event.character.luck} luck
        """)

    @staticmethod
    def enemy_created(event: EnemyCreated) -> None:
        print(GameListener.WHITE + f"""
        New enemy was created with:
            {event.character.strength} strength,
            {event.character.defence} defence,
            {event.character.resource} mana,
            {event.character.speed} speed,
            {event.character.health} health,
            {event.character.luck} luck
        """)

    @staticmethod
    def game_ended(event: GameEnded) -> None:
        print(GameListener.FAIL
              + f"""
        The game has ended.
        Our hero had {event.fights} fights
        And lasted {event.rounds} rounds in the last fight
        """)

    @staticmethod
    def fight_ended(event: FightEnded) -> None:
        fighter = list(filter(lambda character: character.alive, event.fighters)).pop()
        print(GameListener.WARNING + f"The fight has ended. {fighter.character_type} won the fight")

    @staticmethod
    def skill_used(event: SkillUsed) -> None:
        print(GameListener.WHITE
              + f"The {event.attacker.character_type} used {event.skill.get_name()} on {event.defender.character_type}")

    @staticmethod
    def took_damage(event: TookDamage) -> None:
        print(GameListener.WHITE + f"The {event.character.character_type} took {event.value} damage")

    @staticmethod
    def reacted_skill(event: ReactedSkill) -> None:
        print(GameListener.WHITE + f"The {event.character.character_type} reacted with {event.skill.get_name()}")

    @staticmethod
    def character_died(event: CharacterDied) -> None:
        print(GameListener.WARNING + f"The {event.character.character_type} died. RIP!")
