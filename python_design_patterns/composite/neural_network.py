# Let's explore the composite design pattern with the example of a neural network.
from collections.abc import Iterable


class Connectable(Iterable):
    def connect_to(self, other):
        if self == other:
            return

        for self_elem in self:
            for other_elem in other:
                self_elem.outputs.append(other_elem)
                other_elem.inputs.append(self_elem)


class Neuron(Connectable):
    def __init__(self, name: str) -> None:
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f"{self.name}, number of inputs: {len(self.inputs)}, number of outputs: {len(self.outputs)}"

    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for idx in range(count):
            self.append(Neuron(f"{name}-{idx}"))

    def __str__(self):
        return f"{self.name} with {len(self)} neurons"


if __name__ == "__main__":

    neuron_1 = Neuron("n1")
    neuron_2 = Neuron("n2")
    layer_1 = NeuronLayer("L1", 3)
    layer_2 = NeuronLayer("L2", 4)

    neuron_1.connect_to(neuron_2)
    neuron_1.connect_to(layer_1)
    layer_1.connect_to(neuron_2)
    layer_1.connect_to(neuron_2)

    print(neuron_1)
    print(neuron_2)
    print(layer_1)
    print(layer_2)