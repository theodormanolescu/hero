from __future__ import annotations

from Application import EventDispatcher
from Domain.Character import TookDamage
from Domain.Character import CharacterDied
from Domain.Skill.ReactedSkill import ReactedSkill
from Domain.Skill.Skill import Skill
from Domain.Skill.SkillUsed import SkillUsed
from Domain.Character.ActionInterface import ActionInterface
from Domain.Character.StatsInterface import StatsInterface


class Character:
    def __init__(self, dispatcher: EventDispatcher, health=1,
                 resource=1, strength=0,
                 defence=0, speed=0,
                 luck=0, character_type=StatsInterface.ENEMY, ):
        self.health = health
        self.max_health = health
        self.resource = resource
        self.max_resource = resource
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck
        self.alive = True
        self.skills: dict[str, Skill] = {}
        self.character_type = character_type
        self.dispatcher: EventDispatcher = dispatcher

    def regenerate_resource(self) -> None:
        self.resource = min(self.resource + 10, self.max_resource)

    def act(self, action: ActionInterface, another_character: Character) -> None:
        self.try_to_take_action(action, another_character)

    def react(self, action: ActionInterface, skill: Skill) -> None:
        react_skill = self.skills[action.react(self)]
        self.dispatcher.dispatch(ReactedSkill(self, react_skill))
        self.take_damage(
            react_skill.process_value(skill.process_value(self.defence))
        )

    def take_damage(self, value):
        self.dispatcher.dispatch(TookDamage.TookDamage(self, value))
        self.health = max(self.health - value, 0)
        if self.health == 0:
            self.dispatcher.dispatch(CharacterDied.CharacterDied(self))
            self.alive = False

    def add_skill(self, name, skill: Skill) -> None:
        if name not in self.skills:
            self.skills[name] = skill

    def try_to_take_action(self, action: ActionInterface, other_character: Character) -> None:
        skill = self.skills[action.take_action(self)]
        self.dispatcher.dispatch(SkillUsed(self, other_character, skill))

        for count in range(skill.hits):
            other_character.react(action, skill)

    def __lt__(self, other):
        if type(other) is self.__class__:
            return (self.speed, self.luck) > (other.speed, other.luck)
        else:
            return NotImplemented

    def __gt__(self, other):
        if type(other) is self.__class__:
            return (self.speed, self.luck) < (other.speed, other.luck)
        else:
            return NotImplemented
