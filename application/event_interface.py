from abc import abstractmethod


class EventInterface:
    @abstractmethod
    def get_name(self) -> str:
        pass
