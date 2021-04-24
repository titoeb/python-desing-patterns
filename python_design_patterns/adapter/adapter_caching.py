# The adapter design pattern
# A construct which adapts and existing interface X to conform to the required interface Y.
from __future__ import annotations
from typing import List

# Let's construct the interface we have:
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# So we can (kind of) draw points:
def draw_point(p):
    print(".", end="")


# Now let's create two other interfaces:
class Line:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


# But let's imagine we would like to draw a rectangle, e.g. the lines in  rectangle, but
# want to use the `draw_point` interface.
# Let's build an adapter to create Points in a list.
def draw(rectangles: List[Rectangle]):
    for rectangle in rectangles:
        for line in rectangle:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


# So this will be our adapter for line -> point
class LineToPointAdapter:
    count = 0
    cache = {}

    def __init__(self, line: Line):
        super().__init__()
        self.hash = hash(line)
        if self.hash in self.cache:
            return self.cache[self.hash]

        print(
            f"{self.count}: Generating poitns for line"
            f"[{line.start.x}, {line.start.y}]->"
            f"[{line.end.x}, {line.end.y}]"
        )

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []
        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))
        self.cache[self.hash] = points

    def __iter__(self):
        return iter(self.cache[self.hash])


if __name__ == "__main__":
    rectangles = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
    draw(rectangles)

# Nice where can we go from now?
# We could optimize this because currently we build the same points over and over again.