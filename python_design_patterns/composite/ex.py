from collections.abc import Iterable


class Additive:
    @property
    def sum(self):
        return Additive._sum(0, self)

    @staticmethod
    def _sum(aggregate: int, elements: Iterable):
        for elem in elements:
            if hasattr(elem, "__iter__"):
                aggregate = Additive._sum(aggregate, elem)
            else:
                aggregate += elem
        return aggregate


class SingleValue(Additive):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Additive):
    pass


if __name__ == "__main__":
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(23)
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    print(all_values.sum)