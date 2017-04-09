from List import *
from String import String


class Array2D(LiuDataStructure):
    def __init__(self, iterable=[], nrow=1, ncol=1, storage='rows'):

        self.data = List(max_length=nrow)
        self.storage = storage
        self.shape = (nrow, ncol)

        if len(iterable) > 0:
            if isinstance(iterable[0], (int, float)):
                if len(iterable) != ncol * nrow:
                    raise ValueError('the size of the initial values does not match array dimensions')

                for i in range(nrow):
                    new_row = List([0] * ncol, max_length=ncol)

                    for j in range(ncol):
                        index = j * nrow + i if self.storage == 'columns' else i * ncol + j
                        if not isinstance(iterable[index], (int, float)):
                            raise ValueError('initial value must be numeric')
                        new_row[j] = iterable[index]
                    self.data.append(new_row)

            elif isinstance(iterable[0], (list,tuple,List)):
                nrow,ncol=len(iterable), len(iterable[0])
                self.shape = (nrow,ncol)
                self.data = List(max_length=nrow)
                for i in range(nrow):
                    new_row = List([0] * ncol, max_length=ncol)
                    for j in range(ncol):
                        new_row[j] = iterable[i][j]
                    self.data.append(new_row)
        else:
            for i in range(nrow):
                new_row = List([0] * ncol, max_length=ncol)
                self.data.append(new_row)

    def __getitem__(self, slc_obj):

        if isinstance(slc_obj, slice) or isinstance(slc_obj, int):
            return self.data.__getitem__(slc_obj)
        elif isinstance(slc_obj, (list, tuple, List)) and len(slc_obj) > 0 and isinstance(slc_obj[0], int):
            return self.data[slc_obj[0]][slc_obj[1]]
        elif isinstance(slc_obj, (list, tuple, List)) and len(slc_obj) > 0 and isinstance(slc_obj[0], slice):
            vals = [[self.data[ii][jj] for jj in range(*slc_obj[1].indices(self.shape[1]))] for ii in
                    range(*slc_obj[0].indices(self.shape[0]))]
            return Array2D(vals)
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, key, value):
        if isinstance(key, slice) or isinstance(key, int):
            self.data.__getitem__(key,value)
        elif isinstance(key, (list, tuple, List)) and len(key) > 0 and isinstance(key[0], int):
            self.data[key[0]].__setitem__(key[1],value)
        elif isinstance(key, (list, tuple, List)) and len(key) > 0 and isinstance(key[0], slice):
            # vals = [[self.data[ii][jj] for jj in range(*key[1].indices(self.shape[1]))] for ii in
            #         range(*key[0].indices(self.shape[0]))]

            for idxi, i in enumerate(range(*key[0].indices(self.shape[0]))):
                for idxj, j in enumerate(range(*key[1].indices(self.shape[1]))):

                    self.data[i].set(j, value[idxi][idxj])
        else:
            raise TypeError("Invalid argument type.")

    def __copy__(self):
        new_array = Array2D(self.data, self.shape[0], self.shape[1], self.storage)
        return new_array

    def __repr__(self):
        S = String('[ \n')
        for i in range(self.shape[0]):
            s = String('  [')
            for j in range(self.shape[1]):
                s.concatenate(String(' %.1f ' % self[i,j]))
            s.concatenate(String(']\n'))
            S.concatenate(s)
        S.concatenate(String(']'))
        return S.__repr__()

    def __eq__(self, other):
        if self.shape != other.shape:
            raise ValueError('Array dimensions must agree')

        for i in range(self.shape[0]):
            if not self.data[i] == other.data[i]:
                return False

        return True

    def add(self, other):
        if self.shape != other.shape:
            raise ValueError('Array dimensions must agree')

        new_array = self.__copy__()
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array.data[i][j] += other.data[i][j]

        return new_array

    def mul(self, other):
        if self.shape != other.shape:
            raise ValueError('Array dimensions must agree')

        new_array = self.__copy__()
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array.data[i][j] *= other.data[i][j]

        return new_array

    def dot(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError('Array dimensions must agree')

        new_array = Array2D(nrow=self.shape[0], ncol=other.shape[1])

        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                new_array.data[i][j] = sum([self.data[i][k] * other.data[k][j] for k in range(self.shape[1])])

        return new_array

    def isdiag(self):
        return self.shape[0] == self.shape[1]

    def abs(self):
        new_array = self.__copy__()
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array.data[i][j] = abs(new_array.data[i][j])

        return new_array

    def diag(self):
        l = List()
        n = min(self.shape)
        for i in range(n):
            l.append(self.data[i][i])

        return l

    def transpose(self):
        new_array = Array2D(nrow=self.shape[1], ncol=self.shape[0])

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array.data[j][i] = self.data[i][j]

        return new_array


if __name__ == '__main__':
    # a = Array2D(range(16),4,4)
    # a.print()
    #
    # a.mul(a)
    # a.print()
    #
    # a.add(a)
    # a.print()
    #
    # b = a.__copy__()
    # b.print()
    # import numpy as np
    #
    # data = np.arange(36).reshape(4, 9).tolist()
    # a = Array2D(data)
    # print(a[0,1])
    # a.print()
    # a.data.print()
    # a.dot(a.transpose()).print()
    # print(a==a)
    # print(a.diag())
    # print(a.transpose())
    # print(a[3,2])
    # a[3,2]=-4
    # print(a)
    # print(a[0:2, 0:2])
    # a[0:2, 0:2]=[[0,0],[0,0]]
    # print(a)

    a = list(range(25*25))
    b = Array2D(a,25,25)
    print(b)
    print(b[3])