# The interpreter design pattern.
# Turning strings (text) into object oriented structures.

# A component that processe structured text data. It does so by two processes. First, it turns it into
# seperate lexical tokens (lexin). Then it tries to interpretes the tokens (parsing).
from __future__ import annotations
from enum import Enum, auto
from typing import List, Union


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPARENTH = auto()
        RPARENTH = auto()

    def __init__(self, type: Type, text: str):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


def lex(text: str):
    result = []
    idx = 0
    while idx < len(text):
        character = text[idx]
        if character == "+":
            result.append(Token(Token.Type.PLUS, character))
        elif character == "-":
            result.append(Token(Token.Type.MINUS, character))
        elif character == "(":
            result.append(Token(Token.Type.LPARENTH, character))
        elif character == ")":
            result.append(Token(Token.Type.RPARENTH, character))
        else:
            digits = [character]
            for j in range(idx + 1, len(text)):
                if text[j].isdigit():
                    digits.append(text[j])
                    idx += 1
                else:
                    break

            result.append(Token(Token.Type.INTEGER, "".join(digits)))
        idx += 1

    return result


class Integer:
    def __init__(self, value: int):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    def add(self, member: Union[int, BinaryExpression]):
        if self.left is None:
            self.left = member
        elif self.right is None:
            self.right = member
        else:
            raise ValueError(
                "Cant add {member} to {self}, because {self}.left = {self.left} and {self}.right = {self.right}"
            )

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

        elif token.type == Token.Type.LPARENTH:
            j = idx
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPARENTH:
                    break
                else:
                    j += 1
            subexpression = tokens[idx + 1 : j]
            result.add(parse(subexpression))
            idx = j
        idx += 1
    return result


def calc(text: str):
    tokens = lex(text)
    parsed_tokens = parse(tokens)
    print(f"value: {parsed_tokens.value}")


if __name__ == "__main__":
    calc("(13+4)-(12+1)")