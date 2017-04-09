from List import LiuDataStructure, List


class CircularQueue(LiuDataStructure):
    def __init__(self, iterable=[], max_length=16, overwrite=False):
        self.data = List(max_length=max_length,iterable=[None]*max_length)
        self.max_length = max_length
        self.front_index = None
        self.rear_index = None
        self.length = 0
        self.overwrite = overwrite

        if len(iterable) > 0:
            for item in iterable:
                self.enqueue(item)

    def __getitem__(self, slc_obj):
        raise AssertionError("Stack does not support slicing")

    def __setitem__(self, slc_obj):
        raise AssertionError("Stack does not support slicing")

    def __iter__(self):
        while not self.is_empty():
            yield self.dequeue()

    def __repr__(self):
        if self.length > 0:
            string = 'Front-> ['
            for i in range(self.length):
                string += '%s, ' % str(self.data[(self.front_index + i) % self.max_length])

            if self.length > 0:
                string = string[:-2]
            string += '] <- Rear'

            return string
        else:
            string = 'Front-> [] <- Rear'
        return string

    def __getitem__(self, item):
        raise AssertionError("Queue does not support slicing")

    def __setitem__(self, item):
        raise AssertionError("Queue does not support slicing")

    def enqueue(self, item):

        if self.length == self.max_length and self.overwrite is False:
            raise AssertionError("Queue is full")

        self.rear_index = 0 if self.rear_index is None else (self.rear_index + 1) % self.max_length
        # print('en',self.front_index,self.rear_index)
        self.data[self.rear_index] = item

        if self.length == 0:
            self.front_index = self.rear_index
            self.length += 1
        elif self.rear_index != self.front_index:
            self.length += 1
        elif self.rear_index == self.front_index:
            self.front_index = (self.front_index + 1) % self.max_length

        return self

    def dequeue(self):
        if self.length == 0:
            raise AssertionError("Queue is empty.")

        item = self.data[self.front_index]

        if self.length == 1:
            self.front_index = self.rear_index = None
        else:
            self.front_index = (self.front_index + 1) % self.max_length
        # print('de', self.front_index, self.rear_index)
        self.length -= 1

        return item

    def peek(self):
        if self.front_index == None:
            raise AssertionError("Queue is empty.")
        return self.data[self.front_index]

    def clear(self):
        self.data = List(n=self.max_length)
        self.front_index = None
        self.rear_index = None
        self.length = List()

    def is_empty(self):
        return self.length == 0


if __name__ == '__main__':
    s = CircularQueue(iterable=[1,2,3,4,5,6], max_length=8, overwrite=True)
    s.print(prefix='after initialization:')

    s.enqueue(7)
    s.enqueue(8)
    s.enqueue(9)
    s.print('after enqueuing 7,8,9:')

    s.dequeue()
    s.print(prefix='after dequeue():')
    s.dequeue()
    s.print(prefix='after dequeue():')

    s.enqueue(7)
    s.enqueue(8)
    s.enqueue(9)
    s.enqueue(10)
    s.print(prefix='after enqueueing 7,8,9,10 :')

    s.dequeue()
    s.print(prefix='after dequeue():')
    s.dequeue()
    s.print(prefix='after dequeue():')

    s.enqueue(11)
    s.enqueue(12)
    s.print(prefix='after enqueueing 11,12 :')

    #s.enqueue(13)

    while not s.is_empty():
        s.dequeue()
        s.print(prefix='after dequeue():')

    s.enqueue(13)
    s.enqueue(14)
    s.print(prefix='after enqueueing 13,14 :')

