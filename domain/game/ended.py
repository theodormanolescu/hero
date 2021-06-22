from application.event_interface import EventInterface


class Ended(EventInterface):
    def __init__(self, fights: int, rounds: int):
        self.fights: int = fights
        self.rounds: int = rounds

    def get_name(self) -> str:
        return 'game_ended'
