from List import List, LiuDataStructure


class Stack(LiuDataStructure):
    def __init__(self, iterable=[]):
        self.base = List()
        self.top = None
        self.length = 0
        for item in iterable:
            self.push(item)

    def __iter__(self):
        while not self.is_empty():
            yield self.pop()

    def __repr__(self):
        if self.length > 0:
            string = 'Base-> ' + self.base.__repr__() + ' <- Top'
        else:
            string = 'Base-> [ ] <- Top'
        return string

    def __getitem__(self, slc_obj):
        raise AssertionError("Stack does not support slicing")

    def __setitem__(self, slc_obj):
        raise AssertionError("Stack does not support slicing")

    def push(self, item):
        self.base.append(item)
        self.length = self.base.length
        self.top = item
        return self

    def pop(self):
        item = None
        try:
            item = self.base.remove(self.length - 1)
            self.length = self.base.length
            if self.base.length > 0:
                self.top = self.base.get(self.base.length - 1)
            else:
                self.top = None
        except IndexError:
            raise IndexError('Stack is empty')

        return item

    def peek(self):
        return self.top

    def clear(self):
        self.base = List()
        self.top = None
        self.length = 0

    def is_empty(self):
        return self.base.length == 0



if __name__ == '__main__':
    s = Stack(iterable=[3, 4, 5, 76, 2, 6])
    s.print(prefix='after initialization:')
    print('element popped:', s.pop())
    s.print(prefix='after pop():')
    while not s.is_empty():
        s.pop()
        s.print(prefix='after pop():')

    s.push(9)
    s.print()
