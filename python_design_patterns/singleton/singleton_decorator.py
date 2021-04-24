"""The singleton design pattern with a singleton decorator.
The singleton allocator had the issue, that we could call a constructor and the
singleton object might be changed. Let's use a decorator to solve the issue.
"""
from __future__ import annotations
import random


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print(f"Building database {random.randint(0, 100)}")


# Let's check it out!
if __name__ == "__main__":
    database_1 = Database()
    database_2 = Database()
    print(database_1 is database_2)
