from application.event_dispatcher import EventDispatcher
from domain.character.action_interface import ActionInterface
from domain.character.character import Character
from domain.character.character_creation import CharacterCreation
from domain.fight.fight import Fight
from domain.game.ended import Ended
from domain.game.enemy_created import EnemyCreated
from domain.game.hero_created import HeroCreated
from domain.game.started import Started


class Game:
    def __init__(self, dispatcher: EventDispatcher, action: ActionInterface, character_generator: CharacterCreation):
        self.hero: Character = None
        self.enemy: Character = None
        self.action = action
        self.dispatcher = dispatcher.with_subscribers()
        self.character_generator = character_generator
        self.fights = 0
        self.rounds = 0

    def create_hero(self) -> None:
        self.hero = self.character_generator.new_hero()
        self.dispatcher.dispatch(HeroCreated(self.hero))

    def start_game(self, difficulty_level=1) -> None:
        self.dispatcher.dispatch(Started(difficulty_level))
        self.create_hero()

    def is_not_over(self) -> bool:
        return self.hero.alive

    def start_new_fight(self) -> None:
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
            self.hero.regenerate_resource()
        self.fights += 1
        self.rounds = fight.get_rounds()

    def recover(self) -> None:
        self.hero.recover(self.action)

    def create_enemy(self) -> None:
        self.enemy = self.character_generator.new_enemy()
        self.dispatcher.dispatch(EnemyCreated(self.enemy))

    def end_game(self) -> None:
        self.dispatcher.dispatch(Ended(self.fights, self.rounds))
