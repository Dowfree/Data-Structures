# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:45:44 2016

@author: jiajun
"""

from List import List
from Queue import Queue
from Stack import Stack
import math
from queue import PriorityQueue


class SeqBinaryTree(object):
    def __init__(self, nodes=[]):  # node in format (k,item)
        self.length = 0
        self.max_index = 0

        if len(nodes) > 0:
            max_index = max([node[0] for node in nodes])
            self.data = List(max_length=max_index, iterable=[None] * max_index)
            for node in nodes:
                self.insert(node[0], node[1])

    def insert(self, index, node):  # node in format (k,item)
        path = []
        idx = index
        while idx > 1:
            path.insert(0, math.floor(idx / 2))
            idx = math.floor(idx / 2)
        print('path:', path)

        for i in path:
            if not self.data[i - 1]:
                raise ValueError('Missing node @ %d' % (i))

        self.data[index - 1] = node
        self.length += 1
        self.max_index = self.max_index if self.max_index > index - 1 else index - 1

    def traverse_pre(self, index=0):

        if index > self.max_index or self.data[index] is None:
            return ''

        s = '%s ' % (self.data[index])

        pre_index = 2 * index + 1
        if pre_index <= self.max_index:
            s += self.traverse_pre(pre_index)

        post_index = 2 * (index + 1)
        if post_index <= self.max_index:
            s += self.traverse_pre(post_index)

        return s

    def traverse_in(self, index=0):

        if index > self.max_index or self.data[index] is None:
            return ''

        s = ''
        pre_index = 2 * index + 1
        if pre_index <= self.max_index:
            s += self.traverse_in(pre_index)

        s += '%s ' % (self.data[index])

        post_index = 2 * (index + 1)
        if post_index <= self.max_index:
            s += self.traverse_in(post_index)

        return s

    def traverse_post(self, index=0):

        if index > self.max_index or self.data[index] is None:
            return ''

        s = ''
        pre_index = 2 * index + 1
        if pre_index <= self.max_index:
            s += self.traverse_post(pre_index)

        post_index = 2 * (index + 1)
        if post_index <= self.max_index:
            s += self.traverse_post(post_index)

        s += '%s ' % (self.data[index])

        return s

    def traverse_level(self):

        s = ''
        for i in range(self.max_index + 1):
            if self.data[i] is not None:
                s += '%s ' % (self.data[i])

        return s

    def _build_str(self, index):

        if index < 0 or index > self.max_index or self.data[index] is None:
            return 0, 0, 0, []

        line1 = []
        line2 = []
        val_len = gap_len = len(str(self.data[index]))

        l_len, l_val_from, l_val_to, l_lines = self._build_str(2 * index + 1)
        r_len, r_val_from, r_val_to, r_lines = self._build_str(2 * (index + 1))

        if l_len > 0:
            l_anchor = -int(-(l_val_from + l_val_to) / 2) + 1  # ceiling
            line1.append(' ' * (l_anchor + 1))
            line1.append('_' * (l_len - l_anchor))
            line2.append(' ' * l_anchor + '/')
            line2.append(' ' * (l_len - l_anchor))
            val_from = l_len + 1
            gap_len += 1
        else:
            val_from = 0

        line1.append(str(self.data[index]))
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
        if self.length == 0:
            return ''

        return '\n' + '\n'.join(self._build_str(0)[-1])

    def destroy(self):
        pass

    def leftSibling(self, index):
        pass

    def delete(self, index):
        pass


class LinkedBinaryTreeNode(object):
    def __init__(self, item=None, left_child=None, right_child=None):
        self.item = item
        self.left_child = left_child
        self.right_child = right_child

    def __le__(self, other):
        return self.item < other.item

    def __lt__(self, other):
        return self.item < other.item


class LinkedBinaryTree(object):
    def __init__(self, nodes=[]):  # node in format (k,item)
        self.root = None
        self.length = 0
        for node in nodes:
            self.insert(node[0], node[1])

    def insert(self, cue, item):  # node in format (k,item), or ( (parent,order), item)
        path = []
        idx = cue
        while idx > 1:
            path.insert(0, idx % 2)
            idx = math.floor(idx / 2)
        # print('path:', path)

        if len(path) == 0:
            self.root = LinkedBinaryTreeNode(item)
            self.length += 1
            return

        parent = self.root
        for i in range(len(path) - 1):
            if path[i] == 0:
                parent = parent.left_child
            else:
                parent = parent.right_child

        # print(parent)
        if path[-1] == 0:
            parent.left_child = LinkedBinaryTreeNode(item)
        else:
            parent.right_child = LinkedBinaryTreeNode(item)

        self.length += 1

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

    def traverse_level(self):

        s = ''

        q = Queue([self.root])

        while not q.is_empty():
            n = q.dequeue()

            if n:
                s += '%s ' % n.item

                if n.left_child is not None:
                    q.enqueue(n.left_child)

                if n.right_child is not None:
                    q.enqueue(n.right_child)

        return s

    def traverse_in_non_recur(self):

        stack = Stack([self.root])
        s = ''
        visited = set()

        while not stack.is_empty():
            p = stack.peek()
            while p.left_child and p.left_child not in visited:
                stack.push(p.left_child)
                p = p.left_child

            node = stack.pop()
            s += "%s " % str(node.item)
            visited.add(node)

            if p.right_child and p.right_child not in visited:
                stack.push(p.right_child)

        return s

    def traverse_pre_non_recur(self):

        stack = Stack([self.root])
        s = ''

        while not stack.is_empty():
            p = stack.pop()
            s += "%s " % str(p.item)

            if p.right_child:
                stack.push(p.right_child)
            if p.left_child:
                stack.push(p.left_child)

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

    def find(self, item):
        return self._find(self.root, item)

    def _find(self, node, item):

        if node:
            if node.item == item:
                return True, '', node

            res = self._find(node.left_child, item)
            if res[0]:
                return True, '0' + res[1], res[2]

            res = self._find(node.right_child, item)
            if res[0]:
                return True, '1' + res[1], res[2]

        return False, '', None


class ThreadedBinaryTreeNode(object):
    def __init__(self, item=None, left_child=None, right_child=None, left_tag=0, right_tag=0):
        self.item = item
        self.left_child = left_child
        self.right_child = right_child
        self.left_tag = left_tag
        self.right_tag = right_tag


class HuffmanTree(LinkedBinaryTree):
    def __init__(self, data=[]):  # data: [(probability,char),...]
        self.data = data
        self.length = len(data)
        q = PriorityQueue()
        for node in data:
            q.put((node[0], LinkedBinaryTreeNode(node[1])), False)

        n1 = q.get(False)
        while not q.empty():
            n2 = q.get(False)
            n = LinkedBinaryTreeNode('%.2f' % (n1[0] + n2[0]), n1[1], n2[1])
            q.put((n1[0] + n2[0], n), False)
            n1 = q.get(False)
            self.length += 1

        self.root = n1[1]

    def __repr__(self):
        s = super(HuffmanTree, self).__repr__()
        s += '\n'
        for c in [i[1] for i in self.data]:
            s += '%s:%s\n' % (c, self.encode(c))
        return s

    def encode(self, char):

        res = self.find(char)
        if res[0]:
            return res[1]
        else:
            raise ValueError('%s not in code table' % char)

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
            line1.append(' ' * (l_anchor))
            line1.append('0')
            line1.append('_' * (l_len - l_anchor if l_len - l_anchor else 1))
            line2.append(' ' * l_anchor + '/')
            line2.append(' ' * (l_len - l_anchor if l_len - l_anchor else 1))
            val_from = l_len + 1
            gap_len += 1 + (0 if l_len - l_anchor else 1)
        else:
            val_from = 0

        line1.append(str(node.item))
        line2.append(' ' * val_len)

        if r_len > 0:
            r_anchor = int((r_val_from + r_val_to) / 2)  # floor
            pad = 0 if r_anchor else 1
            line1.append('_' * max(r_anchor, 1))
            line1.append('1')
            line1.append(' ' * (r_len - r_anchor))
            line2.append(' ' * (r_anchor + pad) + '\\')
            line2.append(' ' * (r_len - r_anchor))
            gap_len += 1 + pad
        val_to = val_from + val_len - 1

        gap = ' ' * gap_len
        lines = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_lines), len(r_lines))):
            l_line = l_lines[i] if i < len(l_lines) else ' ' * l_len
            r_line = r_lines[i] if i < len(r_lines) else ' ' * r_len
            lines.append(l_line + gap + r_line)

        return len(lines[0]), val_from, val_to, lines


class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, data=[]):
        self.root = None
        self.length = 0
        for item in data:
            self.insert(item)

    def insert(self, item):
        if self.root is None:
            self.root = LinkedBinaryTreeNode(item)
            self.length += 1
            return

        found, node = self.find(item)

        if item <= node.item:
            node.left_child = LinkedBinaryTreeNode(item)
        else:
            node.right_child = LinkedBinaryTreeNode(item)

        self.length += 1

    def find(self, item):
        if self.root is None:
            return False, None

        node = self.root

        while True:
            finished = True
            while item > node.item and node.right_child:
                node = node.right_child
                finished = False
            while item <= node.item and node.left_child:
                node = node.left_child
                finished = False
            if finished:
                break

        if node == item:
            return True, node
        else:
            return False, node

    def find_item(self, item, parent=None):
        if parent==None:
            if self.root:
                parent=self.root
                if parent.item == item:
                    return True, None, -1, parent

                return self.find_item(item,parent)

        if item <= parent.item and parent.left_child:
            if parent.left_child.item == item:
                return True, 0, parent.item, parent.left_child.item
            else:
                res = self.find_item(item, parent.left_child)
                if res[0]:
                    return res

        elif item > parent.item and parent.right_child:
            if parent.right_child.item == item:
                return True, 1, parent, parent.right_child
            else:
                res = self.find_item(item, parent.right_child)
                if res[0]:
                    return res
        return False, None, -1, None

    def remove(self, item):
        found, side, parent, node = self.find_item(item)

        if found:
            l_child = node.left_child
            r_child = node.right_child

            if side == 1:
                if l_child:
                    parent.right_child = l_child
                    node = l_child
                    while node.right_child:
                        node = node.right_child
                    node.right_child = r_child
                else:
                    parent.right_child = r_child
            else:
                if r_child:
                    parent.left_child = r_child
                    node = r_child
                    while node.left_child:
                        node = node.left_child
                    node.left_child = l_child
                else:
                    parent.left_child = l_child
