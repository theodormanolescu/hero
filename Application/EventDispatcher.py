from Application.EventInterface import EventInterface
from Domain.Game.GameListener import GameListener


class EventDispatcher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def dispatch(self, event: EventInterface):
        for subscriber in self.subscribers:
            for method in dir(subscriber):
                if event.get_name() == method:
                    getattr(subscriber, method)(event)

    def with_subscribers(self):
        self.add_subscriber(GameListener())
        return self
