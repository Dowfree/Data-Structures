# -*- coding utf-8 -*-

import sys
import unittest


class LiuDataStructure:
    def print(self, prefix='', postfix=''):
        print(prefix + self.__repr__() + postfix)

    def __getitem__(self, slc_obj):
        if isinstance(slc_obj, slice):
            # Get the start, stop, and step from the slice

            return self.__class__([self[ii] for ii in range(*slc_obj.indices(len(self)))])
        elif isinstance(slc_obj, int):
            if slc_obj < 0:  # Handle negative indices
                slc_obj += len(self)
            if slc_obj < 0 or slc_obj >= len(self):
                raise IndexError("The index (%d) is out of range." % slc_obj)
            return self.get(slc_obj)  # Get the data from elsewhere
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, slc_obj, sequence):

        #print('key value', item, sequence)
        if isinstance(slc_obj, slice):
            # Get the start, stop, and step from the slice
            for idx, i in enumerate(range(*slc_obj.indices(len(self)))):
                # print(i,sequence[idx])
                self.set(i, sequence[idx])
            return

        elif isinstance(slc_obj, int):
            if slc_obj < 0:  # Handle negative indices
                slc_obj += len(self)
            if slc_obj < 0 or slc_obj >= len(self):
                raise IndexError("The index (%d) is out of range." % slc_obj)
            return self.set(slc_obj, sequence)  # Get the data from elsewhere
        else:
            raise TypeError("Invalid argument type.")

    def __iter__(self):
        for i in range(self.length):
            yield self.data[i]

    def __len__(self):
        return self.length

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for idx, val in enumerate(self):
                if self[idx] != other[idx]:
                    return False
            return True


class List(LiuDataStructure):
    def __init__(self, iterable=[], max_length=16):
        try:
            self.length = 0
            self.data = [None] * max_length
            self.max_length = max_length

        except MemoryError as e:
            print('List creation failed:', e)
            print(sys.exc_info()[0])
        for item in iterable:
            self.insert(self.length, item)

    def insert(self, index, item):

        if index < 0 or index > self.length:
            raise IndexError('Index out of bound')

        if self.length == self.max_length:
            new_data = [None] * self.max_length * 2
            for i in range(self.max_length):
                new_data[i] = self.data[i]
            self.data = new_data
            self.max_length *= 2

        if self.length > 0:
            for i in range(self.length - 1, index - 1, -1):
                self.data[i + 1] = self.data[i]

        self.data[index] = item
        self.length += 1
        return self

    def get(self, index):

        if index < 0 or index >= self.length:
            raise IndexError('Index out of bound')

        return self.data[index]

    def set(self, index, item):

        if index < 0 or index >= self.length:
            raise IndexError('Index out of bound')
        self.data[index] = item
        return self.data[index]

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError('Index out of bound')

        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        self.length -= 1

        return item

    def find(self, item):
        for i in range(0, self.length):
            if item == self.data[i]:
                return i

        return -1

    def __repr__(self):
        string = '['
        for i in range(0, self.length):
            string += str(self.data[i]) + ', '
        if self.__len__() > 0:
            string = string[:-2]
        string += ']'
        return string

    def append(self, item):
        self.insert(self.length, item)
        return self


class TestList(unittest.TestCase):
    def test_constructor(self):
        l = self.tested_class(range(5))

        if self.tested_class == List:

            self.assertEqual(l.data[:5], list(range(5)))
            self.assertEqual(l.data[5:], [None] * (l.max_length - 5))
            self.assertEqual(len(l), 5)
            self.assertEqual(l.max_length, len(l.data))

            l = self.tested_class()
            self.assertEqual(l.data, [None] * l.max_length)
            self.assertEqual(len(l), 0)
            self.assertEqual(l.max_length, len(l.data))
        else:
            self.assertEqual(l, self.tested_class([0, 1, 2, 3, 4]))
            self.assertEqual(len(l), 5)
            self.assertEqual(l.head.next.data, 0)
            self.assertEqual(l.tail.data, 4)

    def test_insert_remove(self):
        l = self.tested_class(range(5))
        l.insert(0, 6)
        self.assertEqual(l, self.tested_class([6, 0, 1, 2, 3, 4]))
        self.assertEqual(len(l), 6)

        l.insert(6, 7)
        self.assertEqual(l, self.tested_class([6, 0, 1, 2, 3, 4, 7]))
        self.assertEqual(len(l), 7)

        item = l.remove(0)
        self.assertEqual(item, 6)
        self.assertEqual(l, self.tested_class([0, 1, 2, 3, 4, 7]))
        self.assertEqual(len(l), 6)

        with self.assertRaises(IndexError):
            l.insert(-1, 10)

        with self.assertRaises(IndexError):
            l.remove(6)

    def test_slicing(self):

        l = self.tested_class(range(10))
        self.assertEqual(l[:6], self.tested_class([0, 1, 2, 3, 4, 5]))
        self.assertEqual(l[::2], self.tested_class([0, 2, 4, 6, 8]))
        self.assertEqual(l[-1:0:-2], self.tested_class([9, 7, 5, 3, 1]))
        self.assertEqual(l[4], 4)
        self.assertEqual(l[:-4], self.tested_class([0, 1, 2, 3, 4, 5]))

        l[2] = 8
        self.assertEqual(l, self.tested_class([0, 1, 8, 3, 4, 5, 6, 7, 8, 9]))
        l[2:6] = (0, 1, 2, 3)
        self.assertEqual(l, self.tested_class([0, 1, 0, 1, 2, 3, 6, 7, 8, 9]))
        l[2:8:2] = (3, 5, 7)
        self.assertEqual(l, self.tested_class([0, 1, 3, 1, 5, 3, 7, 7, 8, 9]))

        l[-2:-8:-2] = (-3, -5, -7)
        self.assertEqual(l, self.tested_class([0, 1, 3, 1, -7, 3, -5, 7, -3, 9]))


if __name__ == '__main__':

    TestList.tested_class = List.List
    unittest.main()

    l = List(max_length=8)
    # l.print()

    for i in range(10):
        l.insert(0, i)
    l.print()

    print(l.remove(3))
    l.print()

    l.insert(3, 6)
    l.print()

    # l.insert(11,3)
    # l.remove(10)

    print(l.find(5))

    print(l[9:0:-2])
