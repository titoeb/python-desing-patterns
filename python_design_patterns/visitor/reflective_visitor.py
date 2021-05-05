# The visitor pattern.
# This time implemented in a seperate class.
from abc import ABC


class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value


class Expression(ABC):
    pass


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter(Expression):
    @staticmethod
    def print(expression, buffer):
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(")")


Expression.print = lambda self, buffer: ExpressionPrinter.print(self, buffer)


if __name__ == "__main__":
    expression = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )

    buffer = []
    expression.print(buffer)
    print("".join(buffer))
