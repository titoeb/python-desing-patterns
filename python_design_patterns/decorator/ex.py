class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        if hasattr(self.shape, "resize"):
            self.shape.resize(factor)

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


if __name__ == "__main__":
    circle = ColoredShape(Circle(5), "red")
    assert str(circle) == "A circle of radius 5 has the color red", str(circle)

    circle.resize(2)
    assert str(circle) == "A circle of radius 10 has the color red", str(circle)
