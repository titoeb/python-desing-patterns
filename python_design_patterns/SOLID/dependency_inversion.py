from __future__ import annotations
import abc
from enum import Enum
from typing import List, Tuple

# The depency inversion principle
# High level modules should not depend on low-level module, but they should depend on abstractions.
# Therefore, one should rather depend on interfaces then concrete implementations.


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name: str):
        self.name: str = name

    def __str__(self):
        return self.name


# This is the lower level module that does not use other classes and even more importantly
# it handles lower level mechanics like storage.
class Relationships:
    def __init__(self):
        self.relations: List[Tuple[int]] = []

    def add_parent_and_child(self, parent: int, child: int):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))


# This is the higher level module in the sense that is uses other classes and does not handle
# lower level machanics.
class Resarch:
    def __init__(self, relationships: Relationships):
        for person_0, relationship_type, person_1 in relationships.relations:
            if person_0.name == "John" and relationship_type == Relationship.PARENT:
                print(f"John has a child called {person_1.name}")


# So what is the problem with the Research class?
# Well it depends on the low level object Relationships, in particular on the fact
# that the relations in there are stored as a list. If we decide at a later point to
# use a dictionary or a database instead, we will break the research class!

# So what to do?
# First, we should not use the object `relations` of the `Relationships` class directly,
# but we should use dedicated methods to access the information. Even better we should
# define an interace instead of depending on the lower level class (relationships) directly!

# So let's define the `RelationshipBrowser`!
class RelationshipBrowser:
    @abc.abstractmethod
    def find_all_children_of(self, name):
        pass


class BetterRelationships(RelationshipBrowser):
    def __init__(self):
        self.relations: List[Tuple[int]] = []

    def add_parent_and_child(self, parent: int, child: int):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for person_0, relationship_type, person_1 in self.relations:
            if person_0.name == name and relationship_type == Relationship.PARENT:
                yield person_1


class BetterResarch:
    def __init__(self, browser: RelationshipBrowser):
        for person in browser.find_all_children_of("John"):
            print(f"John has a child called {person}")


if __name__ == "__main__":
    parent = Person("John")
    child1 = Person("Chris")
    child2 = Person("Matt")

    relations = Relationships()
    relations.add_parent_and_child(parent=parent, child=child1)
    relations.add_parent_and_child(parent=parent, child=child2)

    research = Resarch(relationships=relations)

    # Using these objects, it satisfies the dependency inversion principle:
    better_relations = BetterRelationships()
    better_relations.add_parent_and_child(parent=parent, child=child1)
    better_relations.add_parent_and_child(parent=parent, child=child2)

    better_research = BetterResarch(browser=better_relations)
