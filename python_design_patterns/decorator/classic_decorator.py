# A decorator facilitates the addition of behaviors to individual objects
# without inheriting from them.

# Let's now look at the "classical" decorator.
from abc import ABC


class Shape(ABC):
    def __str__(self) -> str:
        return ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius = self.radius * factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"


# This is our decorator-class
class ColoredShape(Shape):
    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape, transperency) -> None:
        self.shape = shape
        self.transperency = transperency

    def __str__(self):
        return f"{self.shape} has {self.transperency * 100}% transperency"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    # Now add a color into the circle without modifying the class structure.
    red_circle = ColoredShape(circle, "red")
    print(red_circle)

    red_half_transparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_circle)

    # We could even stack multiple decorators
    red_green_color = ColoredShape(red_half_transparent_circle, "green")
    print(red_green_color)