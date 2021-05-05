# The visitor design pattern.
# A visitor is a component that knows how to travers a data structure composed of (possible related) types.

# This implementation of the "intrusive visitor" modifies the already existing classes and therefore
# goes against the open-closed principle.


class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))

    def eval(self):
        return self.value


class AdditionExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append("(")
        self.left.print(buffer)
        buffer.append("+")
        self.right.print(buffer)
        buffer.append(")")

    def eval(self):
        return self.left.eval() + self.right.eval()


if __name__ == "__main__":
    expression = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )

    buffer = []
    expression.print(buffer)

    print("".join(buffer))

    print(expression.eval())