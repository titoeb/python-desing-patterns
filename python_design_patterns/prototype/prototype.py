""" The prototype design pattern.
The prototype design pattern should be used if you don't want to always initiallize an object from scratch
but sometimes have maybe a few standard, potentially partially initialized object. Then, a copy of such a
prototype can be the starting point to creating your final object."""
from __future__ import annotations
from copy import deepcopy


class Address:
    def __init__(self, street_address: str, city: str, country: str) -> None:
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives in {self.address}"


if __name__ == "__main__":
    john = Person("John", Address("123 London Road", "Lodon", "UK"))
    print(john)

    # Now we can use John as a prototype for other persons,
    # the only thing we need in the `copy.deepcopy` funtion.
    jane = deepcopy(john)
    jane.name = "Jane"
    print(jane)