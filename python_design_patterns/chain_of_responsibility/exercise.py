class Creature:
    pass


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        self.game = game
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        if self in self.game.creatures:
            return self.initial_attack + self.game.hasKing
        else:
            return self.initial_attack

    @property
    def defense(self):
        if self in self.game.creatures:
            return self.initial_defense + self.game.n_goblins - 1
        else:
            return self.initial_defense


class GoblinKing(Goblin):
    def __init__(self, game):
        self.game = game


class Game:
    def __init__(self):
        self.creatures = []

    @property
    def hasKing(self):
        for creature in self.creatures:
            if isinstance(creature, GoblinKing):
                return True
        return False

    @property
    def n_goblins(self):
        return len(self.creatures)

    def append(self, obj):
        self.creatures.append(obj)
        return self


if __name__ == "__main__":
    game = Game()
    goblin = Goblin(game)
    game.creatures.append(goblin)

    print(goblin.attack, goblin.defense)
    assert goblin.attack == 1
    assert goblin.defense == 1

    goblin_2 = Goblin(game)
    goblin_3 = Goblin(game)
    game.append(goblin_2).append(goblin_3)

    print(goblin.attack, goblin.defense)
    assert goblin.attack == 1
    assert goblin.defense == 3

    goblin_king = GoblinKing(game)
    game.append(goblin_king)

    print(goblin.attack, goblin.defense)
    assert goblin.attack == 2
    assert goblin.defense == 4