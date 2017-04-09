# -*- coding:utf-8 -*-

from BinaryTree import LinkedBinaryTree
from queue import PriorityQueue


class LinkedBinaryTreeNode(object):
    def __init__(self, item=None, left_child=None, right_child=None):
        self.item = item
        self.left_child = left_child
        self.right_child = right_child

    def __le__(self, other):
        return self.item < other.item

    def __lt__(self, other):
        return self.item < other.item


class HuffManTree(LinkedBinaryTree):
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
        s = super(HuffManTree, self).__repr__()
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

    def decode(self, char):
        s = ''
        node = self.root
        for i in char:
            if i == '0' and node.left_child:
                node = node.left_child
            if i == '1' and node.right_child:
                node = node.right_child
            if not node.right_child and not node.left_child:
                s += node.item
                node = self.root
        return s
