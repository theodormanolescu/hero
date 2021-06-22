from application.event_dispatcher import EventDispatcher
from domain.character.action_interface import ActionInterface
from domain.character.character import Character
from domain.fight.ended import Ended
from domain.fight.started import Started


class Fight:
    STACK_ITERATIONS = 5

    def __init__(self, dispatcher: EventDispatcher, action: ActionInterface, character_list):
        self.list: list[Character] = character_list
        self.stack: list[int] = []
        self.action: ActionInterface = action
        self.dispatcher: EventDispatcher = dispatcher
        self.rounds: int = 0
        self._is_not_over = True
    # todo: use teams green/blue to allow multiple characters

    def start(self):
        self._get_action_order()
        self._create_action_stack()
        self.dispatcher.dispatch(Started())

    def do_battle(self):
        attacker = self._get_attacker()
        defender = self._get_defender()
        attacker.act(self.action, defender)
        if attacker.alive and defender.alive:
            defender.act(self.action, attacker)
        if not attacker.alive or not defender.alive:
            self._is_not_over = False

    def _get_attacker(self) -> Character:
        return self.list[self.stack.pop()]

    def _get_defender(self) -> Character:
        return self.list[self.stack.pop()]

    def is_not_over(self) -> bool:
        if not self._is_not_over:
            self.dispatcher.dispatch(Ended(self.list))
        return self._is_not_over

    def get_rounds(self) -> int:
        return self.rounds

    def next_turn(self) -> None:
        if len(self.stack) == 0:
            self._create_action_stack()
        self.rounds += 1

    def _get_action_order(self) -> None:
        self.list.sort()

    def _create_action_stack(self) -> None:
        for iteration in range(Fight.STACK_ITERATIONS):
            for index in range(len(self.list)):
                self.stack.append(index)
        self.stack.reverse()
