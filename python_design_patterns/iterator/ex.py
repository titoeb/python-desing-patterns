from __future__ import annotations


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        def traverse(current: Node):
            yield current
            if current.left:
                for node in traverse(current.left):
                    yield node
            if current.right:
                for node in traverse(current.right):
                    yield node

        for node in traverse(self):
            yield node.value


if __name__ == "__main__":
    #   1
    #  / \
    # 2   3

    root = Node(value=1, left=Node(value=2), right=Node(value=3))

    for value in root.traverse_preorder():
        print(value)
