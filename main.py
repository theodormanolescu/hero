from Application.EventDispatcher import EventDispatcher
from Domain.Character.CharacterCreation import CharacterCreation
from Domain.Game.Game import Game
from Infrastructure.Character.InMemoryCharacterRepository import InMemoryCharacterRepository
from Infrastructure.Skill.InMemorySkillRepository import InMemorySkillRepository
from Input.RandomActionGenerator import RandomActionGenerator
from Input.RandomStatsGenerator import RandomStatsGenerator

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
