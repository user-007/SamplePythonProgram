class Node:
    def __init__(self, value):
        self._value = value
        self.children = []

    def __repr__(self):
        return 'Node({!r}'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
