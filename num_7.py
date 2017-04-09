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

A = [[0.0764, 0.0090, 0.0326, 0.0367, 0.1472, 0.0107, 0.0087, 0.0074, 0.0753, 0.0061, 0.0005, 0.0546, 0.0297, 0.0710,0.0580, 0.0252, 0.0136, 0.0669, 0.0795, 0.0724, 0.0631, 0.0184, 0.0007, 0.0043, 0.0013, 0.0033],[0.0652, 0.0189, 0.0273, 0.0508, 0.1640, 0.0166, 0.0301, 0.0458, 0.0655, 0.0027, 0.0142, 0.0344, 0.0253, 0.0978,0.0259, 0.0067, 0.0002, 0.0700, 0.0727, 0.0615, 0.0417, 0.0085, 0.0192, 0.0003, 0.0004, 0.0113],[0.1153, 0.0222, 0.0402, 0.0501, 0.1218, 0.0069, 0.0177, 0.0070, 0.0625, 0.0049, 0.0001, 0.0497, 0.0316, 0.0671,0.0868, 0.0251, 0.0088, 0.0687, 0.0798, 0.0463, 0.0293, 0.0114, 0.0002, 0.0022, 0.0101, 0.0047]]
a1, a2, a3 = [], [], []
for i in range(26):
    a1.append((A[0][i], chr(65+i)))
    a2.append((A[1][i], chr(65 + i)))
    a3.append((A[2][i], chr(65 + i)))
b1 = HuffManTree(a1)
b2 = HuffManTree(a2)
b3 = HuffManTree(a3)
c1 = '0011001010110011110001110101000010111000011110010101101101000111000011110011001001110000011001011110101101100110'
c2 = '1101011000011000000101110100011100011110110000011010111011001011101011001001011110011000110001010001001001'
c3 = '00000111110101011001010101111100001110001010110110001111111001010111001111010010011001110111101011100000111111111'
print(b1.decode(c1))
print(b2.decode(c2))
print(b3.decode(c3))