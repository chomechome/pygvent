import unittest

from pygvent.structure import Node
from pygvent.utils.reference import WeakReference


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.node = Node()

    def test_get_parent_when_no_parent(self):
        self.assertIsNone(self.node.get_parent())

    def test_get_parent(self):
        parent = Node()

        self.node._parent = WeakReference(parent)

        self.assertIs(parent, self.node.get_parent())

    def test_attach(self):
        parent = Node()

        parent.attach(self.node)

        self.assertIs(parent, self.node.get_parent())
        self.assertIn(self.node, parent._children)

    def test_attach_with_index(self):
        parent = Node()
        parent.attach(Node())

        parent.attach(self.node, index=0)

        self.assertEqual(0, parent._children.index(self.node))

    def test_detach_when_no_parent(self):
        self.node.detach()

        self.assertIsNone(self.node._parent)

    def test_detach(self):
        parent = Node()

        parent.attach(self.node)
        self.node.detach()

        self.assertIsNone(self.node.get_parent())
        self.assertNotIn(self.node, parent._children)

    def test_reattach(self):
        old_parent = Node()
        new_parent = Node()

        old_parent.attach(self.node)
        new_parent.attach(self.node)

        self.assertIs(new_parent, self.node.get_parent())
        self.assertIn(self.node, new_parent._children)
        self.assertNotIn(self.node, old_parent._children)

    def test_children(self):
        first = Node()
        second = Node()

        self.node.attach(first)
        self.node.attach(second)

        self.assertSequenceEqual([first, second], list(self.node.children))

    def test_walk(self):
        first = Node()
        second = Node()
        third = Node()
        fourth = Node()

        self.node.attach(first)
        first.attach(second)
        first.attach(third)
        second.attach(fourth)

        expected = [first, second, fourth, third]
        self.assertSequenceEqual(expected, list(self.node.walk()))

    def test_weak_reference_to_parent(self):
        Node().attach(self.node)
        self.assertIsNone(self.node.get_parent())
