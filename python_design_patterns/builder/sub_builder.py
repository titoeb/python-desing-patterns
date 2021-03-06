"""In this script we explore using sub-builders with a fluent interface to jump from one
to another."""
from __future__ import annotations
from typing import Optional
from copy import copy


class Person:
    def __init__(
        self,
        street_adress: Optional[str] = None,
        postcode: Optional[str] = None,
        city: Optional[str] = None,
        company_name: Optional[str] = None,
        position: Optional[str] = None,
        annual_income: Optional[str] = None,
    ):
        # Adress
        self.street_adress = street_adress
        self.postcode = postcode
        self.city = city
        # Employment
        self.company_name = company_name
        self.position = position
        self.annual_income = annual_income

    def __str__(self):
        return (
            f"Adress: {self.street_adress}, {self.postcode}, {self.city} "
            f"Employed at {self.company_name} as a {self.position} earning {self.annual_income}"
        )


# Let's create some builders for the person!
class PersonBuilder:
    def __init__(self, person: Person) -> None:
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAdressBuilder(self.person)

    def build(self) -> Person:
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def at(self, company_name: str):
        self.person.company_name = company_name
        return self

    def as_a(self, position: str):
        self.person.position = position
        return self

    def earning(self, earning: int):
        self.person.earning = earning
        return self


class PersonAdressBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def at(self, street_adress: str):
        self.person.street_adress = street_adress
        return self

    def in_city(self, city: str):
        self.person.city = city
        return self

    def with_postcode(self, postcode: str):
        self.person.postcode = postcode
        return self


# Let's actually use our builder patterns!
person_builder = PersonBuilder(
    Person(),
)
person_engineer = (
    person_builder.lives.at("123 London Road")
    .in_city("London")
    .with_postcode("SW12BC")
    .works.at("Fabrikam")
    .as_a("Engineer")
    .earning(123000)
    .build()
)

print(person_engineer)
person_manager = (
    person_builder.lives.at("321 London Road")
    .in_city("Berlin")
    .with_postcode("SW12BC")
    .works.at("Google")
    .as_a("Manager")
    .earning(123001)
    .build()
)

print(person_manager)
print(person_builder.person)

# What I really don't like about this, is how the state of the person builder is handled.
# It would be great if you could use the `person_builder` object more thant once, and that's
# also what the name suggests to me. Unfortunately, as the internal `person` object will be stored,
# this fluent interface has really confusing side effects as it does change the unterlying person builder
# object.
