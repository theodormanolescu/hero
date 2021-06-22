import unittest

from application.event_dispatcher import EventDispatcher
from application.event_interface import EventInterface
from domain.character.character import Character
from domain.character.took_damage import TookDamage


class MyTestCase(unittest.TestCase):
    def test_that_it_can_take_damage(self):
        dispatcher = EventDispatcher()

        def dispatch(event: EventInterface):
            self.assertEqual(event.value, 20)

        dispatcher.dispatch = dispatch
        character = Character(dispatcher, health=100)
        character.take_damage(20)
        self.assertEqual(80, character.health)

    def test_that_it_can_die(self):
        dispatcher = EventDispatcher()

        def dispatch(event: EventInterface):
            if isinstance(event, TookDamage):
                self.assertEqual(event.value, 110)
            else:
                self.assertEqual(event.get_name(), 'character_died')

        dispatcher.dispatch = dispatch
        character = Character(dispatcher, health=100)
        character.take_damage(110)
        self.assertEqual(0, character.health)
        self.assertEqual(False, character.alive)


if __name__ == '__main__':
    unittest.main()
