# The proxy design pattern.


class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading the image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


def draw_image(image):
    print("About to draw image.")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    bitmap = Bitmap("facepalm.jpg")
    draw_image(bitmap)

# What is the problem here?
# We are loading the image in  the constructor, even if we never use it
# Of course, we could change the class directly, but we could also use a proxy
# for that purpose!


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    @property
    def bitmap(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        return self._bitmap

    def draw(self):
        self.bitmap.draw()


if __name__ == "__main__":
    bitmap = LazyBitmap("facepalm.jpg")
    draw_image(bitmap)
