"""The Factory method
The factory method is a pattern that is can be applied when the object creation becomes too convoluted.
It pushes the object creation in a seperate (static) function."""
from __future__ import annotations
from enum import Enum
from math import sin, cos


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


# So far so good. But let's say you want to also initiallize coordinates from other coordinate
# systems? You could do the following:


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class NewPoint:
    def __init__(self, a: float, b: float, cordinate_system: CoordinateSystem) -> None:
        if cordinate_system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif cordinate_system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = b * cos(a)
        else:
            raise AttributeError(f"Cordinate system {cordinate_system} is not known!")

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


# Great. Or is it? Really it is very inconvenient for multiple reasons:
# It breaks the open-close principle as for each new way to inputing coordinates,
# we have to change the logic of the constructor again.
# Even more important, the construction is hard to understand. a, b have different
# interpretations depending on what was specified in coordinate_system, also
# it is not clear if a->x and b->y or vice versa.

# Let's use the the factory method!
class Point:
    # Constructor for simple, cartesian cordinates
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # factory method for polar coordinates.
    @classmethod
    def create_cartesian_point(cls, x: float, y: float) -> Point:
        return cls(x=x, y=y)

    @classmethod
    def create_polar_point(cls, rho: float, theta: float) -> Point:
        return cls(x=rho * cos(theta), y=theta * sin(rho))

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


# Let's use the factory methods!
if __name__ == "__main__":
    default_point = Point(2.0, 3.0)
    print(f"default point: {default_point}")

    polar_point = Point.create_polar_point(1.0, 2.0)
    print(f"poloar point: {polar_point}")

    cartesian_point = Point.create_cartesian_point(2.0, 3.0)
    print(f"cartesian point: {cartesian_point}")


# Cool, so what is a factory now?
# A factory is a class that produces other classes. So in this example
# we would group together the two classmethods that are constructors
# from the Point class into a distinct PointFactory class like so:
class PointFactory:
    @staticmethod
    def create_cartesian_point(x: float, y: float) -> Point:
        return Point(x=x, y=y)

    @staticmethod
    def create_polar_point(rho: float, theta: float) -> Point:
        return Point(x=rho * cos(theta), y=theta * sin(rho))


# Using it now looks very similar:
if __name__ == "__main__":
    polar_point = PointFactory.create_polar_point(1.0, 2.0)
    print(f"poloar point: {polar_point}")

    cartesian_point = PointFactory.create_cartesian_point(2.0, 3.0)
    print(f"cartesian point: {cartesian_point}")
