from List import LiuDataStructure
from Stack import Stack


class Hanoi(LiuDataStructure):
    def __init__(self, n_plates=5):
        self.n_plates = n_plates
        self.tower_a = Stack(range(n_plates, 0, -1))
        self.tower_b = Stack()
        self.tower_c = Stack()

    def __repr__(self):
        return '----------------\nA: %s\nB: %s\nC: %s\n----------------\n' % ( \
            str(self.tower_a), str(self.tower_b), str(self.tower_c))

    def __move(self, origin, dest):
        item = origin.pop()
        if len(dest) > 0 and dest.peek() < item:
            raise AssertionError
        dest.push(item)
        self.print()

    def __solve_recursive(self, origin, dest, swap, n):
        if n == 1:
            self.__move(origin, dest)
            return
        print('moving', n)
        self.__solve_recursive(origin, swap, dest, n - 1)
        self.__move(origin, dest)
        self.__solve_recursive(swap, dest, origin, n - 1)

    def solve_recursive(self):
        self.__solve_recursive(self.tower_a, self.tower_c, self.tower_b, self.n_plates)

    def solve_stack(self):
        call_stack = Stack()
        call_stack.push(('call',self.tower_a, self.tower_c, self.tower_b, self.n_plates))

        while not call_stack.is_empty():
            cmd, o, d, s, n = call_stack.pop()
            if cmd == 'move':
                self.__move(o,d)
                #self.print()
            else:
                if n == 1:
                    call_stack.push(('move', o, d, None, None))
                else:
                    call_stack.push(('call', s, d, o, n - 1))
                    call_stack.push(('move', o, d, None, None))
                    call_stack.push(('call', o, s, d, n - 1))



if __name__ == '__main__':
    h = Hanoi(5)
    #h.print()
    h.solve_stack()
    #h.solve_recursive()
    #h.print()
