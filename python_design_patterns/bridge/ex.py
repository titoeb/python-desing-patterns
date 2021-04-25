from abc import ABC


class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Triangle"

    def __str__(self):
        return self.renderer.render_triangle


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Square"

    def __str__(self):
        return self.renderer.render_square


# imagine VectorTriangle and RasterTriangle are here too
class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def render_triangle(self):
        return f"Drawing Triangle as lines"

    @property
    def render_circle(self):
        return f"Drawing Circle as lines"


class RasterRenderer(Renderer):
    @property
    def render_triangle(self):
        return f"Drawing Triangle as pixels"

    @property
    def render_circle(self):
        return f"Drawing Circle as pixels"


# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
if __name__ == "__main__":

    print(str(Triangle(RasterRenderer())))