from abc import abstractmethod

class ActionInterface:
    @abstractmethod
    def take_action(self, character: 'Character') -> str:
        pass

    @abstractmethod
    def react(self, character: 'Character') -> str:
        pass
