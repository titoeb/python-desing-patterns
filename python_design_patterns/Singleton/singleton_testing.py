""" 
"""
from __future__ import annotations
import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        with open("capitals.txt", "r") as file_handler:
            lines = file_handler.readlines()

        for idx in range(0, len(lines), 2):
            self.population[lines[idx].strip()] = int(lines[idx + 1].strip())


class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for city in cities:
            result += Database().population[city]
        return result


class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(
        self,
        cities,
    ):
        result = 0
        for city in cities:
            result += self.db.population[city]
        return result


class DummyDB:
    population = {"a": 1, "b": 2}

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    # The main problem with the folowing test, and generally singeletons in this case
    # is that we test on a "live"-database. How can me make this more save?
    def test_singleton_population(self):
        record_finder = SingletonRecordFinder()
        names = ["Bonn", "Munique"]
        total_population = record_finder.total_population(cities=names)
        self.assertEqual(10 - 1, total_population)

    dummy_db = DummyDB()

    def test_dependent_population(self):
        configurable_record_finder = ConfigurableRecordFinder(self.dummy_db)
        self.assertEqual(3, configurable_record_finder.total_population(["a", "b"]))


if __name__ == "__main__":
    unittest.main()
