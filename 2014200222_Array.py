from List import *
from String import String


class Array2D(LiuDataStructure):
    def __init__(self, iterable=[], nrow=1, ncol=1, storage='rows'):

        self.data = List(max_length=nrow*ncol)
        self.storage = storage
        self.shape = (nrow, ncol)

        if len(iterable) > 0:
            if isinstance(iterable[0], (int, float)):
                if len(iterable) != ncol * nrow:
                    raise ValueError('the size of the initial values does not match array dimensions')

                for i in range(nrow*ncol):
                    if not isinstance(iterable[i], (int, float)):
                        raise ValueError('initial value must be numeric')
                    self.data.append(iterable[i])

            elif isinstance(iterable[0], (list, tuple, List)):
                nrow, ncol = len(iterable), len(iterable[0])
                self.shape = (nrow, ncol)
                self.data = List(max_length=nrow*ncol)
                for i in range(nrow):
                    for j in range(ncol):
                        self.data.append(iterable[i][j])
        else:
            for i in range(nrow*ncol):
                self.data.append(0)

    def __getitem__(self, slc_obj):
        if isinstance(slc_obj, slice):
            new_row = []
            for i in range(*slc_obj.indices(self.shape[0])):
                new_row.append(self.data[i*self.shape[1]:(i+1)*(self.shape[1])])
            return Array2D(new_row)
        elif isinstance(slc_obj, int):
            return self.data[slc_obj*self.shape[1]:(slc_obj+1)*self.shape[1]]
        elif isinstance(slc_obj, (list, tuple, List)) and len(slc_obj) > 0 and isinstance(slc_obj[0], int):
            return self.data[slc_obj[0]*self.shape[1]+slc_obj[1]]
        elif isinstance(slc_obj, (list, tuple, List)) and len(slc_obj) > 0 and isinstance(slc_obj[0], slice):
            vals = [[self.data[ii*self.shape[1]+jj] for jj in range(*slc_obj[1].indices(self.shape[1]))] for ii in
                    range(*slc_obj[0].indices(self.shape[0]))]
            return Array2D(vals)
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            for idx, i in enumerate(range(*key.indices(self.shape[0]))):
                index = slice(i * (self.shape[1]), (i + 1) * (self.shape[1]), 1)
                self.data.__setitem__(index, value[idx])
        elif isinstance(key, int):
            index = slice(key * (self.shape[1]), (key + 1) * (self.shape[1]))
            self.data.__setitem__(index, value)
        elif isinstance(key, (list, tuple, List)) and len(key) > 0 and isinstance(key[0], int):
            self.data.__setitem__(key[0] * (self.shape[1]) + key[1], value)
        elif isinstance(key, (list, tuple, List)) and len(key) > 0 and isinstance(key[0], slice):
            for idxi, i in enumerate(range(*key[0].indices(self.shape[0]))):
                for idxj, j in enumerate(range(*key[1].indices(self.shape[1]))):
                    self.data[i * (self.shape[1]) + j] = value[idxi][idxj]
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
                s.concatenate(String(' %.1f ' % self.data[i*self.shape[1]+j]))
            s.concatenate(String(']\n'))
            S.concatenate(s)
        S.concatenate(String(']'))
        return S.__repr__()

    def __eq__(self, other):
        if self.shape != other.shape:
            raise ValueError('Array dimensions must agree')

        for i in range(self.shape[0]*self.shape[1]):
            if not self.data[i] == other.data[i]:
                return False

        return True

    def add(self, other):
        if self.shape != other.shape:
            raise ValueError('Array dimensions must agree')

        new_array = self.__copy__()
        for i in range(self.shape[0]*self.shape[1]):
                new_array.data[i] += other.data[i]
        return new_array

    def mul(self, other):
        if self.shape != other.shape:
            raise ValueError('Array dimensions must agree')

        new_array = self.__copy__()
        for i in range(self.shape[0]*self.shape[1]):
                new_array.data[i] *= other.data[i]
        return new_array

    def dot(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError('Array dimensions must agree')

        new_array = Array2D(nrow=self.shape[0], ncol=other.shape[1])

        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                new_array.data[i*other.shape[1]+j] = sum([self.data[i*self.shape[1]+k] * other.data[k*other.shape[1]+j] for k in range(self.shape[1])])
        return new_array

    def isdiag(self):
        return self.shape[0] == self.shape[1]

    def abs(self):
        new_array = self.__copy__()
        for i in range(self.shape[0]*self.shape[1]):
                new_array.data[i] = abs(new_array.data[i])
        return new_array

    def diag(self):
        l = List()
        n = min(self.shape)
        for i in range(n):
            l.append(self.data[i*self.shape[1]+i])
        return l

    def transpose(self):
        new_array = Array2D(nrow=self.shape[1], ncol=self.shape[0])
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_array.data[j*self.shape[0]+i] = self.data[i*self.shape[1]+j]
        return new_array
