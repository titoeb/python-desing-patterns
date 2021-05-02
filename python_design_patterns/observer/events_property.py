# The observer design pattern.
# An observer is an object that whishes to be informed aobut events happening
# in the system. The entitiy generating the events is an observable.
from __future__ import annotations


class Event(list):
    def __call__(self, *args, **kwargs):
        for fun in self:
            fun(*args, **kwargs)


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age: int = 0):
        super().__init__()
        self._age = age

    @property
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_value: int):
        if not self._age == new_value:
            old_can_vote = self.can_vote
            self._age = new_value
            self.property_changed("age", new_value)
            if old_can_vote != self.can_vote:
                self.property_changed("can_vote", self.can_vote)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name, value):
        if name == "age":
            if value < 16:
                print("Sorry you still cannot drive")
            else:
                print("You can drive now! :)")
                self.person.property_changed.remove(self.person_changed)


def person_changed(name, value):
    if name == "can_vote":
        print(f"Voting ability changed to value {value}")


if __name__ == "__main__":
    person = Person()
    person.property_changed.append(person_changed)
    traffic_authority = TrafficAuthority(person)
    for age in range(14, 20):
        print(f"Setting age to {age}")
        person.age = age
