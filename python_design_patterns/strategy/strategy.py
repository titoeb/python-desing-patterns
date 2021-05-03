# The strategy design pattern.
# Enables the exact behaviour of a system to be selected at run-time.
from __future__ import annotations
from typing import List
from abc import ABC
from enum import Enum, auto

# This is our blueprint for the algoritm
class ListStrategy(ABC):
    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass


# This is one potential algoritm
class MarkdonwListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        return buffer.append(f" * {item}\n")


# This is another potential algoritm
class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f" <li>{item}</li>\n")


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


# And this is now a different part of the algorithm that works with
# different versions of the `ListStrategy`
class TextProcessor:
    def __init__(self, list_strategy: ListStrategy = HtmlListStrategy()):
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items: List[str]):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)

        self.list_strategy.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdonwListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
        else:
            raise ValueError(f"Format {format} is not known.")

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == "__main__":
    items = ["foo", "bar", "baz"]
    text_processor = TextProcessor()
    text_processor.set_output_format(OutputFormat.MARKDOWN)
    text_processor.append_list(items)
    print(text_processor)

    text_processor.clear()
    text_processor.set_output_format(OutputFormat.HTML)
    text_processor.append_list(items)
    print(text_processor)