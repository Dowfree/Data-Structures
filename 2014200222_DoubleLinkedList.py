# -*- coding utf-8 -*-
import sys

"""双向链表及链表的反转"""

class LiuDataStructure:
    def print(self,prefix='',postfix=''):
        print(prefix+self.__repr__()+postfix)

class Node(LiuDataStructure):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

class LinkedList(LiuDataStructure):
    def __init__(self, iterable=[]):
        self.head = Node(None)
        self.length = 0
        for item in iterable: self.insert(self.length,item)

    def __repr__(self):
        (current, nodes) = self.head.next, []
        while  current :
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

        pn = p.next
        p.next = node
        node.next = pn

        self.length += 1
        return self

    def remove(self, index):
        if index < 0 or index > self.length:
            raise IndexError

        q = p = self.head
        for i in range(index):
            q = p
            p = p.next

        q.next = p.next
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

    def reverse(self):
        p = None
        while self.head.next:
            q = self.head.next
            self.head.next = q.next
            q.next = p
            p = q
        self.head.next= p

    def merge_linked_lists(la,lb):
        la.print('la:')
        lb.print('lb:')

        if la.head.next == None: return lb
        if lb.head.next == None: return la

        if la.head.next.data > lb.head.next.data:
            dest, pb, pa = lb, la.head.next, lb.head.next
        else:
            dest, pa, pb = la, la.head.next, lb.head.next

        q = dest.head
        while pb :
            while pa and pa.data <= pb.data:
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

class DoubleLinkedList(LiuDataStructure):
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
        return '['+"<->".join(nodes)+']'

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