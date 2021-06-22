from Application.EventInterface import EventInterface


class GameStarted(EventInterface):
    def __init__(self, difficulty_level):
        self.difficulty_level = difficulty_level

    def get_name(self) -> str:
        return 'game_started'
