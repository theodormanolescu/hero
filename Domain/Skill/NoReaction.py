from Domain.Skill.Skill import Skill


class NoReaction(Skill):
    NAME = 'no_reaction'

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return NoReaction.NAME

    def process_value(self, modifier: int) -> int:
        return modifier
