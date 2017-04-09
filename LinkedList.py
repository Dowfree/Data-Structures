from List import LiuDataStructure


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
        self.tail = Node(None)
        self.length = 0
        for item in iterable: self.append(item)

    def __repr__(self):
        (current, nodes) = self.head.next, []
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return '[' + " -> ".join(nodes) + ']'

    def __iter__(self):
        p = self.head
        while p.next is not None:
            data = p.next.data
            p = p.next
            yield data

    def insert(self, index, item):
        if index < 0 or index > self.length:
            raise IndexError('Index out of bound')

        node = Node(item)

        p = self.head
        for i in range(index):
            p = p.next

        pn = p.next
        p.next = node
        node.next = pn

        if index == self.length:
            self.tail = node

        self.length += 1

        return self

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index out of bound')

        q = self.head
        p = q.next
        for i in range(index):
            q = p
            p = p.next

        if p is not None:
            q.next = p.next
        else:
            q.next = None
        data = p.data
        del p

        if index == self.length - 1:
            self.tail = q

        self.length -= 1
        return data

    def append(self, item):
        self.insert(self.length, item)
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index out of bound')

        p = self.head.next
        for i in range(index):
            p = p.next

        return p.data

    def set(self, index, item):
        if index < 0 or index >= self.length:
            raise IndexError('Index out of bound')

        p = self.head.next
        for i in range(index):
            p = p.next

        p.data = item
        return self

    def find(self, item):
        p = self.head

        i = 0
        while p.data != item and p.next != None:
            p = p.next
            i += 1

        if p and p.data == item:
            return i - 1
        else:
            return -1

    def merge_linked_lists(la, lb):
        la.print('la:')
        lb.print('lb:')

        if la.head.next == None: return lb
        if lb.head.next == None: return la

        if la.head.next.data > lb.head.next.data:
            dest, pb, pa = lb, la.head.next, lb.head.next
        else:
            dest, pa, pb = la, la.head.next, lb.head.next

        q = dest.head
        while pb:
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
        lens = len(la), len(lb)
        dest.length = sum(lens)
        return dest


if __name__ == '__main__':
    from List import TestList
    import unittest



    la = LinkedList([2, 6, 9, 13])
    lb = LinkedList([5, 7, 8, 9, 10, 14, 15, 16, 17])
    print(la)
    print(la.remove(0))
    print(la)


