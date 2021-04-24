"""The abstract Factory
The abstract factory is a pattern that is can be applied when the object creation becomes too convoluted.
It pushes the object creation in a seperate class."""

from __future__ import annotations
from enum import Enum
from abc import ABC

# The abstract base class.
class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious!")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious!")


class HotDrinkFactory(ABC):
    @staticmethod
    def prepare(amount: int):
        pass


class TeaFactory:
    @staticmethod
    def prepare(amount: int):
        print("Make tea.")
        return Tea()


class CoffeeFactory:
    @staticmethod
    def prepare(amount: int):
        print("Make coffee.")
        return Coffee()


def make_drink(drink_type: str):
    if drink_type == "tea":
        return TeaFactory.prepare(10)
    elif drink_type == "coffee":
        return CoffeeFactory.prepare(10)
    else:
        raise AttributeError(f"drink {drink_type} is not known!")


# Great so far, but is the reason for having the abstract base class? Let's see:
class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = 1
        TEA = 2

    factories = []
    initiallized = False

    def __init__(self) -> None:
        if not self.initiallized:
            self.initiallized = True
            for drink in self.AvailableDrink:
                name = drink.name[0] + drink.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        all_factories = "\n".join(name for name, _ in self.factories)
        print(f"Available drinks: {all_factories}")
        idx = int(input(f"Please pick a drink (0-{len(self.factories)-1}): "))
        amount = int(input("Specify amount: "))
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    # entry = input("What kind of drink what you like?")
    # drink = make_drink(entry)
    # drink.consume()

    hot_drink_machine = HotDrinkMachine()
    hot_drink_machine.make_drink()