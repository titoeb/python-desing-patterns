# The bridge design pattern.
# It is used to connect components together through abstraction. By doing so it prevents a 'Cartesian product` complexity explosion.
from __future__ import annotations
from abc import ABC

# Let's take the following scenario:
# You have a circle and a square.
# You have a raster and a vector implementation.
# How avoid the 2x2 cartesian product complexity explosion?


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster_renderer = RasterRenderer()
    vector_renderer = VectorRenderer()

    circle = Circle(vector_renderer, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

    circle = Circle(raster_renderer, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
