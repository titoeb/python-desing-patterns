from unittest import TestCase, main as unittest_main
import unittest
from math import isnan
from cmath import sqrt
from abc import ABC


def compute_discriminent(a, b, c):
    return b ** 2 - 4 * a * c


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return compute_discriminent(a, b, c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = compute_discriminent(a, b, c)
        if discriminant < 0:
            return float("nan")
        else:
            return discriminant


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = sqrt(disc)
        return ((-b + root_disc) / (2 * a), (-b - root_disc) / (2 * a))


class Evaluate(TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(isnan(results[0].real))
        self.assertTrue(isnan(results[1].real))
        self.assertTrue(isnan(results[0].imag))
        self.assertTrue(isnan(results[1].imag))


if __name__ == "__main__":
    unittest_main()