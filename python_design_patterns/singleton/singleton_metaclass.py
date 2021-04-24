"""The singleton design pattern with a metaclass.
This is a direct alternative to the decorator for the singleton design pattern.
"""
from __future__ import annotations
import random


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print(f"Building database {random.randint(0, 100)}")


# Let's check it out!
if __name__ == "__main__":
    database_1 = Database()
    database_2 = Database()
    print(database_1 is database_2)
