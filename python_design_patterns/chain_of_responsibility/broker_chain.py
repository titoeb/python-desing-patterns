# The chain of responsibility pattern.
# In the previous example `method_chain.py` we looked into how we can chain operation
# that are then called via `handle()`. But how could we do it immediatly without doing any
# additional action?
from enum import Enum

# Event
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, create_name, what_to_query, default_value) -> None:
        self.create_name = create_name
        self.what_to_query = what_to_query
        self.value = default_value


# Event broker (observer)
class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier:
    def __init__(self, game, creature) -> None:
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            sender.name == self.creature.name
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value *= 2


class Creature:
    def __init__(self, game, name, attack, defense):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game, "Strong Goblin", 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)
    print(goblin)
