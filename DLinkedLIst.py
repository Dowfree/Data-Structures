# -*- coding utf-8 -*-
from List import LiuDataStructure

class Node(LiuDataStructure):
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.data)

class DLinkedList(LiuDataStructure):
    def __init__(self,iterable=[]):
        self.head = Node(None)
        self.tail = Node(None)
        self.length = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        for item in iterable:
            self.insert(self.length, item)

    def __repr__(self):
        (current, nodes) = self.head.next, []
        while current.next:
            nodes.append(str(current))
            current = current.next
        return '['+"->".join(nodes)+']'

    def insert(self, index, val):
        if index < 0 or index > self.length:
            raise IndexError

        node = Node(val)

        p = self.head
        for i in range(index):
            p = p.next

        if p.next is None:
            p.next = self.tail

        pn = p.next
        p.next = node
        pn.prev = node
        node.prev = p
        node.next = pn

        self.length += 1
        return self

    def remove(self, index):
        if index < 0 or index > self.length:
            raise IndexError

        p = self.head
        for i in range(index):
            p = p.next

        p.prev.next = p.next
        p.next.prev = p.prev

        del p
        self.length -= 1

        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError

        p = self.head.next
        for i in range(index):
            p = p.next

        return p.data

    def find(self, val):
        p = self.head

        i = 0
        while p.data != val and p.next != None:
            p = p.next
            i += 1

        if p:
            return i
        else:
            return -1

    def merge_linked_lists(la,lb):
        la.print('la:')
        lb.print('lb:')

        if la.head.next.data == None: return lb
        if lb.head.next.data == None: return la

        if la.head.next.data > lb.head.next.data:
            dest, pb, pa = lb, la.head.next, lb.head.next
        else:
            dest, pa, pb = la, la.head.next, lb.head.next

        q = dest.head
        while pb and pb.data:
            while pa and pa.data and pa.data <= pb.data:
                q = pa
                pa = pa.next

            if pa == None:
                q.next = pb
                break
            else:
                tmp = pb.next
                q.next = pb
                pb.next = pa
                pb = tmp
                q = q.next
            dest.print('dest:')
        return dest

    def reverse(self):
        p = self.head.next
        for i in range(self.length):
            pn = p.next
            p.next = p.prev
            p.prev = pn
            p = pn
        p = self.head.next
        q = self.tail.prev
        self.head.next = q
        self.tail.prev = p
        p.next = self.tail
        q.prev = self.head

if __name__ == '__main__':

    l=DLinkedList()
    l.print()

    for i in range(10):
        l.insert(0,i)
    l.print()

    l.remove(3)
    l.print()

    l.insert(3,1)
    l.print()

    print(l.find(5))

    l.reverse()
    l.print()

    la = DLinkedList([2,6,9,13])
    lb = DLinkedList([5, 7, 8, 9, 10, 14, 15, 16, 17])
    merged = DLinkedList.merge_linked_lists(la, lb)
    merged.print('merged')
    print(merged.find(17))