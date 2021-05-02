from unittest import TestCase
import unittest


class Game(list):
    def __init__(self):
        pass


class Rat:
    def __init__(self, game):
        self.game = game
        self.game.append(self)

    @property
    def attack(self):
        return max(len(self.game), 1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.game.remove(self)


class Evaluate(TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)


if __name__ == "__main__":
    unittest.main()