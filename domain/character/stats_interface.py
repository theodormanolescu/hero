class StatsInterface:
    HERO = 'hero'
    ENEMY = 'enemy'

    def set_type(self, character_type: str) -> None:
        raise NotImplemented()

    def get_strength(self) -> int:
        """Will return strength."""
        raise NotImplemented()

    def get_defence(self) -> int:
        """Will return defence."""
        raise NotImplemented()

    def get_speed(self) -> int:
        """Will return speed."""
        raise NotImplemented()

    def get_luck(self) -> int:
        """Will return luck."""
        raise NotImplemented()

    def get_health(self) -> int:
        """Will return health."""
        pass

    def get_intelligence(self) -> int:
        """Will return intelligence."""
        raise NotImplemented()
