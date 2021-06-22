from Application.EventInterface import EventInterface


class FightStarted(EventInterface):

    def get_name(self) -> str:
        return 'fight_started'
