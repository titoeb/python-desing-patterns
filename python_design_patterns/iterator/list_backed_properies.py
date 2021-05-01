# The iterator design pattern.


class Creature:
    _strength = 0
    _agility = 2
    _intelligence = 3

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[self._strength]

    @property.getter
    def strength(self, value):
        self.stats[self._strength] = value

    @property
    def agilility(self):
        return self.stats[self._agility]

    @property.getter
    def agility(self, value):
        self.stats[self._agility] = value

    @property
    def intellegence(self):
        return self.stats[self._intelligence]

    @property.getter
    def intellegence(self, value):
        self.stats[self._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stat)

    @property
    def max_state(self):
        return max(self.stats)

    @property
    def average_state(self):
        return sum(self.stats) / len(self.stats)
