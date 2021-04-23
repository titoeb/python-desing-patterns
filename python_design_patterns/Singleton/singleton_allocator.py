"""The singleton design pattern.
Some components make only sense to be once in a system:
- Database connection
- Object Factory
When the initializer is expensive you may only want to have these components once.
Therefore, you don't want anyone to copy it, change it and create it only lazy when
someone needs it.
"""
from __future__ import annotations
import random


class Database:
    _instance = None

    # In order to  create a singleton in python, we should overwrite the allocator:
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# Let's check it out!
if __name__ == "__main__":
    database_1 = Database()
    database_2 = Database()
    print(database_1 is database_2)

# But there is a problem with that design, if we add an constructor
# it will be called right after `__new__` and different constructions could
# take place.


class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1, 100)
        print(f"id = {id}")

    # In order to  create a singleton in python, we should overwrite the allocator:
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


# Let's check it out!
if __name__ == "__main__":
    database_1 = Database()
    database_2 = Database()
    print(database_1 is database_2)
