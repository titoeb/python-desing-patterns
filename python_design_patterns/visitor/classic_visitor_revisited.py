# The visitor design pattern.

from abc import ABC

# taken from https://tavianator.com/the-visitor-pattern-in-python/


def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + "." + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[: name.rfind(".")]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    method = _methods[(_qualname(type(self)), type(arg))]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# ↑↑↑ LIBRARY CODE ↑↑↑


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value) -> None:
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter(Expression):
    def __init__(self):
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, double_expression):
        self.buffer.append(str(double_expression.value))

    @visitor(AdditionExpression)
    def visit(self, addition_expression):
        self.buffer.append("(")
        self.visit(addition_expression.left)
        self.buffer.append("+")
        self.visit(addition_expression.right)
        self.buffer.append(")")

    def __str__(self):
        return "".join(self.buffer)


class ExpressionEvaluator:
    def __init__(self) -> None:
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, double_expression):
        self.value = double_expression.value

    @visitor(AdditionExpression)
    def visit(self, addition_expression):
        self.visit(addition_expression.left)
        tmp_1 = self.value
        self.visit(addition_expression.right)
        self.value += tmp_1

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    expression = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(DoubleExpression(2), DoubleExpression(3)),
    )
    printer = ExpressionPrinter()
    printer.visit(expression)
    print(printer)

    expression_evaluator = ExpressionEvaluator()
    expression_evaluator.visit(expression)
    print(expression_evaluator)