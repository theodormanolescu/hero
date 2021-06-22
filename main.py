from application.event_dispatcher import EventDispatcher
from domain.character.character_creation import CharacterCreation
from domain.game.game import Game
from infrastructrure.character.repository import InMemoryCharacterRepository
from infrastructrure.skill.repository import InMemorySkillRepository
from input.random_action_generator import RandomActionGenerator
from input.random_stats_generator import RandomStatsGenerator

if __name__ == '__main__':
    dispatcher = EventDispatcher()
    game = Game(
        dispatcher,
        RandomActionGenerator(),
        CharacterCreation(RandomStatsGenerator(), InMemoryCharacterRepository(), InMemorySkillRepository(), dispatcher)
    )
    game.start_game()

    while game.is_not_over():
        game.create_enemy()
        game.start_new_fight()
        game.recover()
    game.end_game()
