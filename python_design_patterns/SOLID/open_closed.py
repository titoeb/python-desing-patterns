# The Open-Close Principle:
from __future__ import annotations
from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products: List[Product], color: Color):
        for p in products:
            if p.color == color:
                yield p

    # So far so good, now the user comes and also wants to
    # filter by size like so:

    def filter_by_size(self, products: List[Product], size: Size):
        for p in products:
            if p.size == size:
                yield p

    # Or filter by both size and color
    def filter_by_size_and_color(
        self, products: List[Product], size: Size, color: Color
    ):
        for p in products:
            if p.size == size and p.color == color:
                yield p

    # Now we have violated the open-closed principle.
    # It states we should only add new functionality via
    # extension and not via modification.


# Better pattern here would be the `Specification` class:
class Specification:
    def is_satisfied(self, product: Product):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(filer, products: List[Product], spec: Specification):
        pass


# Filtering by color done with the Specification pattern:
class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, product: Product):
        return product.color == self.color


# Filtering  by size done with the Specification pattern
class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, product: Product):
        return product.size == self.size


class BetterFilter(Filter):
    def filter(self, products: List[Product], spec: Specification):
        for product in products:
            if spec.is_satisfied(product):
                yield product


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item: Item):
        return all(
            map(lambda specification: specification.is_satisfied(item), self.args)
        )


if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)
    products: List[Product] = [apple, tree, house]

    print(" hi!")
    # Old approach.
    pf = ProductFilter()
    print("Green products (old)): ")
    for product in pf.filter_by_color(products, Color.GREEN):
        print(f"\t- {product.name} is green.")

    bf = BetterFilter()
    print("Green products (new approach)")
    green = ColorSpecification(Color.GREEN)
    for product in bf.filter(products, green):
        print(f"\t- {product.name} is green.")

    print("Large products (new approach)")
    large = SizeSpecification(Size.LARGE)
    for product in bf.filter(products, large):
        print(f"\t- {product.name} is large.")

    print("Large, blue items")
    large_blue = large & ColorSpecification(Color.BLUE)
    for product in bf.filter(products, large_blue):
        print(f"\t- {product.name} is large and blue.")
