# The observer design pattern.
# An observer is an object that whishes to be informed aobut events happening
# in the system. The entitiy generating the events is an observable.


class Event(list):
    def __call__(self, *args, **kwargs):
        for fun in self:
            fun(*args, **kwargs)


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, adress):
    print(f"{name} needs a doctor at {adress}")


if __name__ == "__main__":
    sherlock = Person("Sherlock", "221B Baker St.")
    sherlock.falls_ill.append(
        lambda name, adress: print(f"{name} falls ill at {adress}")
    )
    sherlock.falls_ill.append(call_doctor)
    sherlock.catch_a_cold()

    sherlock.falls_ill.remove(call_doctor)
    sherlock.catch_a_cold()