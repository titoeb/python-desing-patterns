"""The singleton design pattern - the monostate implementation
The monostate implementation puts the construction of the singleton into a super class and the singleton class
is a child.
"""
from __future__ import annotations


class CEO:
    __shared_state = {"name": "Steve", "age": 55}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years ond"


if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    ceo2.age = 77

    # As you can see, we change the field for both ceo's because, we assigned their
    # __dict__ to the same state (e.g. the constant _shared_state-object)
    print(ceo1)
    print(ceo2)

# We could also package this into a base class:
class Monostate:
    _shared_stated = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_stated
        return obj


# Now our CEO class could be child of that base class.
class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_manged = 0

    def __str__(self):
        return f"{self.name} organizes {self.money_manged} money."


if __name__ == "__main__":
    cfo1 = CFO()
    cfo1.name = "Sheryl"
    cfo1.money_manged = 1
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "Ruth"
    cfo2.money_manged = 10
    print(cfo1)
    print(cfo2)
