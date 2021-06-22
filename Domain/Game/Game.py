from Application.EventDispatcher import EventDispatcher
from Domain.Character.Character import Character
from Domain.Character.CharacterCreation import CharacterCreation
from Domain.Fight.Fight import Fight
from Domain.Game.EnemyCreated import EnemyCreated
from Domain.Game.GameEnded import GameEnded
from Domain.Game.GameStarted import GameStarted
from Domain.Game.HeroCreated import HeroCreated
from Input.ActionInterface import ActionInterface


class Game:
    def __init__(self, dispatcher: EventDispatcher, action: ActionInterface, character_generator: CharacterCreation):
        self.hero: Character = None
        self.enemy: Character = None
        self.action = action
        self.dispatcher = dispatcher.with_subscribers()
        self.character_generator = character_generator
        self.fights = 0
        self.rounds = 0

    def create_hero(self):
        self.hero = self.character_generator.new_hero()
        self.dispatcher.dispatch(HeroCreated(self.hero))

    def start_game(self, difficulty_level=1):
        self.dispatcher.dispatch(GameStarted(difficulty_level))
        self.create_hero()

    def is_not_over(self) -> bool:
        return self.hero.alive

    def start_new_fight(self):
        self.rounds = 0
        fight = Fight(
            dispatcher=self.dispatcher,
            action=self.action,
            character_list=[self.hero, self.enemy]
        )
        fight.start()
        while fight.is_not_over():
            fight.do_battle()
            fight.next_turn()
        self.fights += 1
        self.rounds = fight.get_rounds()

    def recover(self):
        pass

    def create_enemy(self):
        self.enemy = self.character_generator.new_enemy()
        self.dispatcher.dispatch(EnemyCreated(self.enemy))

    def end_game(self) -> None:
        self.dispatcher.dispatch(GameEnded(self.fights, self.rounds))
