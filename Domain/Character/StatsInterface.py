from abc import abstractmethod


class StatsInterface:
    HERO = 'hero'
    ENEMY = 'enemy'

    @abstractmethod
    def set_type(self, character_type: str):
        pass

    @abstractmethod
    def get_strength(self) -> int:
        """Will return strength."""
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """Will return defence."""
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """Will return speed."""
        pass

    @abstractmethod
    def get_luck(self) -> int:
        """Will return luck."""
        pass

    @abstractmethod
    def get_health(self) -> int:
        """Will return health."""
        pass

    @abstractmethod
    def get_intelligence(self) -> int:
        """Will return intelligence."""
        pass
