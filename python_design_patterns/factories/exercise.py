class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    idx = 0

    def create_person(self, name):
        self.idx += 1
        return Person(id=self.idx - 1, name=name)
