""" The prototype factory design pattern.
Couldn't we just store our protypes and create them in a Factory?
"""
from __future__ import annotations
from copy import deepcopy


class Address:
    def __init__(self, street_address: str, city: str, suite: int) -> None:
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.suite}"


class Employee:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives in {self.address}"


# Let's now assume we only have two offices where people might work. Therefore,
# we would like to have two prototypes to choose from.
class EmployeeFactory:
    # Static objects of this class.
    main_office_employee = Employee("", Address("123 East Drive", "London", 0))
    aux_office_employee = Employee("", Address("123B East Drive", "London", 0))

    @staticmethod
    def __new_employee(prototype: Employee, name: str, suite: int):
        new_employee = deepcopy(prototype)
        new_employee.name = name
        new_employee.address.suite = suite
        return new_employee

    @staticmethod
    def new_main_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(
            prototype=EmployeeFactory.main_office_employee, name=name, suite=suite
        )

    @staticmethod
    def new_aux_main_office_employee(name: str, suite: int):
        return EmployeeFactory.__new_employee(
            prototype=EmployeeFactory.aux_office_employee, name=name, suite=suite
        )


if __name__ == "__main__":
    # Now let's create two employees from the two offices with our prototype factory.
    john = EmployeeFactory.new_main_office_employee("John", 101)
    print(john)

    jane = EmployeeFactory.new_aux_main_office_employee("Jane", 500)
    print(jane)