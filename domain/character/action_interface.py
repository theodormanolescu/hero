class ActionInterface:
    def take_action(self, character: 'Character') -> str:
        """
        :type character: domain.character.character.Character
        """
        raise NotImplemented()

    def react(self, character: 'Character') -> str:
        """
        :type character: domain.character.character.Character
        """
        raise NotImplemented()

    def rest(self) -> str:
        raise NotImplemented()
