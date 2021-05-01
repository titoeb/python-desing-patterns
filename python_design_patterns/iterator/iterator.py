# The Iterator design pattern.
# An Itertor is an object that facilitates the traversal of a data structure.
from __future__ import annotations


class Node:
    def __init__(self, value: int, left: Node = None, right: Node = None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __iter__(self):
        return InOrderIterator(self)


# This is a stateful iterator
class InOrderIterator:
    def __init__(
        self,
        root: Node,
    ):
        self.root = root
        self.current = root
        self.yielded_start = False
        while self.current.left:
            self.current = self.current.left

    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True
            return self.current

        if self.current.right:
            self.current = self.current.right
            while self.current.left:
                self.current = self.current.left
            return self.current
        else:
            p = self.current.parent
            while p and self.current == p.right:
                self.current = p
                p = p.parent
            self.current = p
            if self.current:
                return self.current
            else:
                raise StopIteration


# Let's do something more light-weight:
def traverse_in_order(root: Node):
    def traverse(current: Node):
        if current.left:
            for node in traverse(current.left):
                yield node
        yield current
        if current.right:
            for node in traverse(current.right):
                yield node

    for node in traverse(root):
        yield node


if __name__ == "__main__":
    #   1
    #  / \
    # 2   3

    root = Node(value=1, left=Node(value=2), right=Node(value=3))
    tree_iter = iter(root)
    print([next(tree_iter).value for x in range(3)])

    for y in traverse_in_order(root):
        print(y.value)
