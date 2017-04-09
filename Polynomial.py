from List import LiuDataStructure

class PolyNode(LiuDataStructure):
    def __init__(self, coef=None, exp=None, next=None):
        self.coef = coef
        self.exp = exp
        self.next = next

    def __repr__(self):
        s = None
        if self.exp == 0:
            s = "%.fX" % (self.coef)
        else:
            s = "%.fX^%d" % (self.coef, self.exp)

        return s

class Polynomial(LiuDataStructure):
    def __init__(self, iterable=[]):
        self.head = PolyNode(None)
        self.length = 0
        for item in iterable: self.insert(*item) #item should be tuple of (coef,exp)

    def __repr__(self):
        string = ''
        for item in self:
            if item.coef < 0:
                string = string[:-1]
            string += ' '+item.__repr__()+' +'
        string = string[:-1]
        return string

    def __iter__(self):
        current = self.head.next
        while current is not None:
            yield current
            current = current.next

    def insert(self, coef, exp):
        p = self.head
        while p.next is not None and p.next.exp < exp:
            p = p.next

        if p.next is None:
            node = PolyNode(coef, exp)
            p.next = node
        elif p.next.exp == exp:
            p.next.coef += coef
            if p.next.coef == 0:
                tmp = p.next
                p.next = p.next.next
        else:
            node = PolyNode(coef, exp, p.next)
            p.next = node

        return self

    def poly_add_1_by_1(self, poly):
        for node in poly:
            self.insert(node.coef, node.exp)

        return self

    def poly_add(self, poly):
        pa = self.head.next
        pb = poly.head.next
        new_head = PolyNode(None,None)
        p = new_head
        while pa  is not None or pb is not None:
            current = None
            if pa is None:
                current = PolyNode(pb.coef,pb.exp)
                pb = pb.next
            elif pb is None:
                current = PolyNode(pa.coef,pa.exp)
                pa = pa.next
            elif pa.exp == pb.exp:
                coef = pa.coef + pb.coef
                exp = pa.exp
                pa = pa.next
                pb = pb.next
                if coef != 0:current = PolyNode(coef, exp)
                else:continue
            elif pa.exp < pb.exp:
                current = PolyNode(pa.coef, pa.exp)
                pa = pa.next
            else:
                current = PolyNode(pb.coef, pb.exp)
                pb = pb.next
            p.next = current
            p = p.next
        self.head = new_head
        return self

if __name__ == '__main__':
    la = Polynomial([(-9,0),(5,3),(2,4),(7,5),(2,7)])
    lb = Polynomial([(9,0),(6,2),(-2,4),(7,5),(8,9)])

    la.print(prefix='a:')
    lb.print(prefix='b:')
    la.poly_add(lb).print(prefix='a+b:')
    #print(la.poly_add_1_by_1(lb))