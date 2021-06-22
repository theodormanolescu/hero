from abc import abstractmethod, ABC


class EventInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass
