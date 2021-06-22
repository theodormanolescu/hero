from domain.character.repository import CharacterRepository


class InMemoryCharacterRepository(CharacterRepository):

    def get_resource_multiplier(self) -> int:
        return 10
