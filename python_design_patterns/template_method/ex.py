from __future__ import annotations
from typing import List
from unittest import TestCase, main as unittest_main
from abc import ABC


class Creature:
    def __init__(self, attack: int, health: int) -> None:
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures: List[Creature]):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index: int, c2_index: int) -> int:
        creature_1 = self.creatures[c1_index]
        creature_2 = self.creatures[c2_index]

        won_1 = self.hit(attacker=creature_1, defender=creature_2)
        won_2 = self.hit(attacker=creature_2, defender=creature_1)

        if (won_1 and won_2) or (not won_1 and not won_2):
            return -1
        else:
            if won_1:
                return c1_index
            else:
                return c2_index

    def hit(self, attacker: Creature, defender: Creature) -> bool:
        pass  # implement this in derive


class TemporaryDamageCardGame(CardGame):
    def __init__(self, creatures):
        super().__init__(creatures)

    def hit(self, attacker: Creature, defender: Creature) -> bool:
        return defender.health - attacker.attack <= 0


class PermanentDamageCardGame(CardGame):
    def __init__(self, creatures: List[Creature]) -> None:
        super().__init__(creatures)

    def hit(self, attacker: Creature, defender: Creature) -> bool:
        defender.health -= attacker.attack
        return defender.health <= 0


class Evaluate(TestCase):
    def test_impasse(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(
            -1, game.combat(0, 1), "Combat should yield -1 since nobody died."
        )
        self.assertEqual(
            -1, game.combat(0, 1), "Combat should yield -1 since nobody died."
        )

    def test_temporary_murder(self):
        c1 = Creature(1, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(1, game.combat(0, 1))

    def test_double_murder(self):
        c1 = Creature(2, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1))

    def test_permanent_damage_death(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 3)
        game = PermanentDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), "Nobody should win this battle.")
        self.assertEqual(1, c1.health)
        self.assertEqual(2, c2.health)
        self.assertEqual(1, game.combat(0, 1), "Creature at index 1 should win this")


if __name__ == "__main__":
    unittest_main()
