from unittest import TestCase, main as unittest_main
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
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception("Key % not found" % key)
    method = _methods[key]
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


class Value:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, value):
        self.buffer.append(str(value))

    @visitor(AdditionExpression)
    def visit(self, addition_expression):
        self.buffer.append("(")
        self.visit(addition_expression.left)
        self.buffer.append("+")
        self.visit(addition_expression.right)
        self.buffer.append(")")

    @visitor(MultiplicationExpression)
    def visit(self, multiplication_expression):
        self.visit(multiplication_expression.left)
        self.buffer.append("*")
        self.visit(multiplication_expression.right)

    def __str__(self):
        return "".join(self.buffer)


class Evaluate(TestCase):
    def test_simple_addition(self):
        simple = AdditionExpression(Value(2), Value(3))
        ep = ExpressionPrinter()
        ep.visit(simple)
        self.assertEqual("(2+3)", str(ep))

    def test_product_of_addition_and_value(self):
        expr = MultiplicationExpression(
            AdditionExpression(Value(2), Value(3)), Value(4)
        )
        ep = ExpressionPrinter()
        ep.visit(expr)
        self.assertEqual("(2+3)*4", str(ep))


if __name__ == "__main__":
    unittest_main()