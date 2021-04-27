# The facade design pattern.
# Balancing complexity and presentation / usability by providing a simple,
# easy to use / understand user interface over a large and sophisticated body of code.

# Let's imagine we build a low level buffer that stores textual information.
class Buffer:
    def __init__(self, width=30, height=20) -> None:
        self.widht = width
        self.height = height
        self.buffer = [" "] * width * height

    def __getitem__(self, item):
        return self.buffer.__getitem__(item)

    def write(self, text):
        self.bugger += text


# A viewport is now a view to a specific buffer.
class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0

    def get_character_at(self, index):
        return self.buffer[index + self.offset]

    def append(self, text):
        self.buffer.write(text)


# Our main class will be the console. It uses buffers and viewports behind the scenes,
# but the main idea is that this is our facade we hide all the complexity behind.
class Console:
    def __init__(self):
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [b]
        self.viewports = [self.current_viewport]

    # This would be part of the facade, a easy to use function to write to the
    # (current) buffer.
    def write(self, text):
        self.current_viewport.buffer.write(text)

    # ... But it is also possible to get down into the actual low-level
    # interfaces.
    def get_char_at(self, index):
        self.current_viewport.get_character_at(index)


if __name__ == "__main__":
    console = Console()
    console.write("hello")
