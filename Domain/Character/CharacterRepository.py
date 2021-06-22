from abc import abstractmethod


class CharacterRepository:

    @abstractmethod
    def get_resource_multiplier(self) -> int:
        pass
