from List import LiuDataStructure
from LinkedList import LinkedList


class Queue(LiuDataStructure):
    def __init__(self, iterable=[]):
        self.data = LinkedList(iterable)
        self.front = None
        self.rear = None
        self.length = 0

        if len(iterable)>0:
            self.front = self.data.get(0)
            self.rear = self.data.tail
            self.length = self.data.length

    def __iter__(self):
        while not self.is_empty():
            yield self.dequeue()

    def __repr__(self):
        if self.length > 0:
            string = 'Front-> ' + self.data.__repr__() + ' <- Rear'
        else:
            string = 'Front-> [] <- Rear'
        return string

    def __getitem__(self, slc_obj):
        raise AssertionError("Queue does not support slicing")

    def __setitem__(self, slc_obj):
        raise AssertionError("Queue does not support slicing")

    def enqueue(self,item):
        self.data.append(item)
        self.length = self.data.length
        self.rear = self.data.tail
        if self.length == 1:
            self.front = item
        return self

    def dequeue(self):
        item = None
        try:
            item = self.data.remove(0)
            self.length = self.data.length
            if self.data.length>0:
                self.front = self.data.get(0)
            else:
                self.front = None
                self.rear = None
        except IndexError:
            raise IndexError('Queue is empty')

        return item

    def peek(self):
        return self.front

    def clear(self):
        self.front = None
        self.rear = None
        self.length = 0
        self.data = LinkedList()

    def is_empty(self):
        return self.length == 0

if __name__ == '__main__':
    s=Queue(iterable=[3,4,5,76,2,6])
    s.print(prefix='after initialization:')
    s.dequeue()
    s.print(prefix='after dequeue():')

    while not s.is_empty():
        s.dequeue()
        s.print(prefix='after dequeue():')

    s.enqueue(9)
    s.enqueue(11)
    s.print()
    while not s.is_empty():
        s.dequeue()
        s.print(prefix='after dequeue():')
    #s.dequeue()