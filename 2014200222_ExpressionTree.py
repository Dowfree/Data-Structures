import math
from ShuntingYard import *
import copy

operator = ['+', '-', '*', '/', '%', '^']


class LinkedBinaryTreeNode(object):
    def __init__(self, item=None, left_child=None, right_child=None):
        self.item = item
        self.left_child = left_child
        self.right_child = right_child

    def __le__(self, other):
        return self.item < other.item

    def __lt__(self, other):
        return self.item < other.item


class ExpressionTree(object):
    def __init__(self, nodes=[]):  # node in format (k,item)
        self.root = None
        self.length = 0
        self.expression = copy.copy(ShuntingYard.digest(nodes))
        expression = ShuntingYard.digest(nodes)
        nodes = []
        for i in range(len(expression)):
            nodes.insert(0, expression.dequeue())
        for node in nodes:
            self.insert(node)

    def insert(self, item, parent=None):
        if self.root is None:
            self.root = LinkedBinaryTreeNode(item)
            self.length += 1
            return

        if parent is None:
            parent = self.root

        if parent.right_child is None:
            parent.right_child = LinkedBinaryTreeNode(item)
            self.length += 1
            return True

        if parent.right_child.item in operator:
            if self.insert(item, parent.right_child):
                return True

        if parent.left_child is None:
            parent.left_child = LinkedBinaryTreeNode(item)
            self.length += 1
            return True

        if parent.left_child.item in operator:
            if self.insert(item, parent.left_child):
                return True

        return False

    def traverse_pre(self, node=0):

        if node == 0:
            node = self.root

        if node is None:
            return ''

        s = '%s ' % (node.item)

        s += self.traverse_pre(node.left_child)
        s += self.traverse_pre(node.right_child)

        return s

    def traverse_in(self, node=0):

        if node == 0:
            node = self.root

        if node is None:
            return ''

        s = ''
        s += self.traverse_in(node.left_child)
        s += '%s ' % (node.item)
        s += self.traverse_in(node.right_child)

        return s

    def traverse_post(self, node=0):

        if node == 0:
            node = self.root

        if node is None:
            return ''
        s = ''
        s += self.traverse_post(node.left_child)
        s += self.traverse_post(node.right_child)
        s += '%s ' % (node.item)

        return s

    def _build_str(self, node):

        if node is None:
            return 0, 0, 0, []

        line1 = []
        line2 = []
        val_len = gap_len = len(str(node.item))

        l_len, l_val_from, l_val_to, l_lines = self._build_str(node.left_child)
        r_len, r_val_from, r_val_to, r_lines = self._build_str(node.right_child)

        if l_len > 0:
            l_anchor = math.ceil((l_val_from + l_val_to) / 2.0) + 1
            line1.append(' ' * (l_anchor + 1))
            line1.append('_' * (l_len - l_anchor))
            line2.append(' ' * l_anchor + '/')
            line2.append(' ' * (l_len - l_anchor))
            val_from = l_len + 1
            gap_len += 1
        else:
            val_from = 0

        line1.append(str(node.item))
        line2.append(' ' * val_len)

        if r_len > 0:
            r_anchor = int((r_val_from + r_val_to) / 2)  # floor
            line1.append('_' * r_anchor)
            line1.append(' ' * (r_len - r_anchor + 1))
            line2.append(' ' * r_anchor + '\\')
            line2.append(' ' * (r_len - r_anchor))
            gap_len += 1
        val_to = val_from + val_len - 1

        gap = ' ' * gap_len
        lines = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_lines), len(r_lines))):
            l_line = l_lines[i] if i < len(l_lines) else ' ' * l_len
            r_line = r_lines[i] if i < len(r_lines) else ' ' * r_len
            lines.append(l_line + gap + r_line)

        return len(lines[0]), val_from, val_to, lines

    def __repr__(self):
        return self._stringify()

    def _stringify(self):
        if self.length == 0:
            return ''

        return '\n' + '\n'.join(self._build_str(self.root)[-1])

    def calculate(self):
        return ShuntingYard.calculate(self.expression)
