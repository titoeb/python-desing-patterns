from __future__ import annotations
from enum import Enum, auto
from typing import List, Type, Union, Dict


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()

    def __init__(self, type: Type, text: str):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


class Integer:
    def __init__(self, value: int):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self, type=None, left=None, right=None):
        self.type = type
        self.left = left
        self.right = right

    def add_int(self, member: Union[int, BinaryExpression]):
        if self.left is None:
            self.left = member
        elif self.right is None:
            self.right = member
        else:
            f"Cannot add {member} to {self}."

    def add_type(self, type: Type):
        if self.type is None:
            self.type = type
            return self
        else:
            return BinaryExpression(type=type, left=self)

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value

        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value


def parse(tokens: List[Token]):
    result = BinaryExpression()
    idx = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token.type == Token.Type.INTEGER:
            result.add(Integer(int(token.text)))

        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION

        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION

        idx += 1
    return result


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        tokens = ExpressionProcessor.lex(expression, self.variables)
        if len(tokens) == 0:
            return 0
        else:
            return ExpressionProcessor.parse(tokens).value

    @staticmethod
    def lex(text: str, variables: Dict[str, int]):
        result = []
        idx = 0
        while idx < len(text):
            character = text[idx]
            if character == "+":
                result.append(Token(Token.Type.PLUS, character))
            elif character == "-":
                result.append(Token(Token.Type.MINUS, character))
            elif character.isdigit():
                digits = [character]
                for j in range(idx + 1, len(text)):
                    if text[j].isdigit():
                        digits.append(text[j])
                        idx += 1
                    else:
                        break
                result.append(Token(Token.Type.INTEGER, "".join(digits)))

            elif character.isalpha():
                variable = [character]
                for j in range(idx + 1, len(text)):
                    if text[j].isalpha():
                        variable.append(text[j])
                        idx += 1
                    else:
                        break
                variable = "".join(variable)
                if variable in variables:
                    result.append(Token(Token.Type.INTEGER, variables[variable]))
                    break
                else:
                    return []
            else:
                raise ValueError(f"Cannot parse {character}")
            idx += 1

        return result

    @staticmethod
    def parse(tokens: List[Token]):
        result = BinaryExpression()
        idx = 0
        while idx < len(tokens):
            token = tokens[idx]
            if token.type == Token.Type.INTEGER:
                result.add_int(Integer(int(token.text)))

            elif token.type == Token.Type.PLUS:
                result = result.add_type(BinaryExpression.Type.ADDITION)

            elif token.type == Token.Type.MINUS:
                result = result.add_type(BinaryExpression.Type.SUBTRACTION)

            idx += 1
        return result


if __name__ == "__main__":

    processor = ExpressionProcessor()
    assert processor.calculate("1+2+xy") == 0

    processor = ExpressionProcessor()
    assert processor.calculate("1+2+3") == 6

    processor = ExpressionProcessor()
    processor.variables = {"x": 3}
    assert processor.calculate("10-2-x") == 5
