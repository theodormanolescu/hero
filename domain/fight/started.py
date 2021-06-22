from application.event_interface import EventInterface


class Started(EventInterface):

    def get_name(self) -> str:
        return 'fight_started'
