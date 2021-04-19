from __future__ import annotations

# The liskov substitution principle


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}, area: self.area"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value


# Now let's create a sub class of Rectangle that breaks
#  the liskov substitution principle
class Square(Rectangle):
    def __init__(self, size: int):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value: int):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value: int):
        self._height = self._width = value


def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected} got {rc.area}")


if __name__ == "__main__":
    rc = Rectangle(2, 3)
    use_it(rc)
    sq = Square(2)
    use_it(sq)

    # How to deal with it in this case?
    # -> Don't create a square class in the first place
    # -> Simply use a rectangle instead, optionally
    # -> Create method `is_square`.
