"""Builder pattern
The builder pattern is concerned with building objects whenever that gets a bit more complicated.
Instead of having a huge constructor with 10+ arguments the builder pattern provides an api for constructing
 an object step-by-step."""
from __future__ import annotations

# Let's look at building HTML objects as an example:
text = "hello"
parts = ["<p>", text, "</p>"]
print("".join(parts))

# We could automate this the following way:
words = ["hello", "world"]
parts = ["<ul>"]
for word in words:
    parts.append(f" <li>{word}</li>")
parts.append("</ul>")
print("\n".join(parts))

# But of course this gets more and more complicated. And if you mess-up
# the order in which to append the tags, you might end-up with a wrong
# html document.
# Let's outsource this to a builder!
class HtmlElement:
    indent_size = 2

    def __init__(self, name: str, text: str) -> None:
        self.name = name
        self.text = text
        self.elements = []

    def _str(self, indent: int) -> str:
        lines = []
        indent_0 = " " * (indent * self.indent_size)
        lines.append(f"{indent_0}<{self.name}>")

        if self.text:
            indent_1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{indent_1}{self.text}")

        for element in self.elements:
            lines.append(element._str(indent + 1))

        lines.append(f"{indent_0}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self._str(0)


# But so far we did only see the actual HTMLElement. But of course
# we want to look into building it. So let's have a look:
class HtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name, text="")

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def __str__(self):
        return str(self.__root)


# So how could we use it?
builder = HtmlBuilder("ul")
builder.add_child("li", "hello")
builder.add_child("li", "world")
print("Ordinary builder: ")
print(builder)

# We could improve this by making this a "fluent" interface.
# this means that we can chain together multiple calls to add child.
class FluentHtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name, text="")

    # Let's also make a fluent constructor:
    @classmethod
    def get_fluent_html_builder(cls, root_name: str) -> FluentHtmlBuilder:
        fluent_html_builder = cls(root_name=root_name)
        return fluent_html_builder

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(HtmlElement(child_name, child_text))

        # This is what is going to make this interface fluent:
        return self

    def __str__(self):
        return str(self.__root)


# So let's use our fluent builder!
fluent_builder = (
    FluentHtmlBuilder.get_fluent_html_builder("ul")
    .add_child("li", "hello")
    .add_child("li", "world")
)
print("Fluent builder: ")
print(fluent_builder)
