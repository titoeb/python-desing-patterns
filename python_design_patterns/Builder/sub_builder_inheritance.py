from __future__ import annotations
from typing import Optional

# In `sub_builders.py` we saw how we can use sub builders with a fluent interface to
# conveniently create complex object.
# A potential issue what that our implementation violated the open-closed principle as the
# super class, the PersonBuilder, needed to be extenden everytime we add a new sub-builder.

# So let's see how we can solve the problem with inheritence.
class Person:
    def __init__(
        self,
        name: Optional[str] = None,
        position: Optional[str] = None,
        date_of_birth: Optional[str] = None,
    ) -> None:
        self.name = name
        self.position = position
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.name} born on {self.date_of_birth} works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name: str) -> PersonInfoBuilder:
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position: str) -> PersonJobBuilder:
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth: str):
        self.person.date_of_birth = date_of_birth
        return self


# Now let's try it out!
person_builder = PersonBirthDateBuilder()
me = person_builder.called("Tim").works_as_a("Data Scientist").born("1/1/1980").build()
print(me)