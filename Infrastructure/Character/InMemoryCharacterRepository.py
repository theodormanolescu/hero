from Domain.Character.CharacterRepository import CharacterRepository


class InMemoryCharacterRepository(CharacterRepository):

    def get_resource_multiplier(self) -> int:
        return 10
