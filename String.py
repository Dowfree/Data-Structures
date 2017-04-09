from List import LiuDataStructure, List


class String(LiuDataStructure):
    def __init__(self, iterable=[], max_length=32):
        max_length = max_length if max_length>len(iterable)+1 else len(iterable)+1
        self.data = List([0]*max_length,max_length=max_length)
        self.length = len(iterable)

        for idx,c in enumerate(iterable):
            if not isinstance(c, str):
                raise ValueError
            self.data[idx] = ord(c)

        self.data[len(iterable)] = ord('\0')


    def __setitem__(self, key, value):
        # print('value',value)
        temp = List(max_length=len(value))
        for c in value:
            # print(c)
            if not isinstance(c, str):
                raise ValueError("The set value must be a string")
            temp.append(ord(c))

        #print('key value', key, temp)

        return LiuDataStructure.__setitem__(self, key, temp)

    def __getitem__(self, key):
        return LiuDataStructure.__getitem__(self, key)

    def __repr__(self):
        #print(self.data)

        l = List()
        for c in self.data:
            if c == ord('\0'):
                break
            l.append(chr(c))
        return ''.join(l)

    def __iter__(self):
        for c in self.data:
            if c == ord('\0'):
                break
            yield chr(c)

    def get(self, index):
        if index < 0 or index >= len(self):
            raise IndexError('Index out of bound')

        return chr(self.data[index])

    def set(self, index, item):
        if isinstance(item, str):
            item = ord(item)
        if index < 0 or index >= len(self):
            raise IndexError('Index out of bound')
        self.data[index] = item
        return self.data[index]

    @staticmethod
    def __isalphabet__(c):
        if isinstance(c, str):
            c = ord(c)

        return String.LOWER_BASE <= c <= String.LOWER_END or String.UPPER_BASE <= c <= String.UPPER_END

    def upper(self):
        i = 0
        for idx, val in enumerate(self.data[:len(self)]):
            if String.LOWER_BASE <= val <= String.LOWER_END:
                self.data[idx] = val + String.UPPER_OFFSET

        return self

    def lower(self):
        for idx, val in enumerate(self.data[:len(self)]):
            if String.UPPER_BASE <= val <= String.UPPER_END:
                self.data[idx] = val - String.UPPER_OFFSET

        return self

    def copy(self, s):
        for idx, val in enumerate(s.data):
            self.data[idx] = val
        self.length = len(s)
        return self

    def isnumeric(self):
        for i in range(len(self)):
            if not chr(self.data[i]) in '0123456789.':
                return False
        return True

    def compare(self, s):

        for idx, val in enumerate(self.data):
            if idx > len(s) + 1 or s.data[idx] < self.data[idx]:
                return 1
            elif s.data[idx] > self.data[idx]:
                return -1
            elif s.data[idx] == self.data[idx] and self.data[idx] != ord('\0'):
                continue
            elif s.data[idx] == self.data[idx] and s.data[idx] == ord('\0'):
                return 0

    def __eq__(self, s):
        return self.compare(s) == 0

    def concatenate(self, s):

        dest = self
        addlen = 1 if isinstance(s,int) else len(s)

        if isinstance(s, str) and len(s) > 1:
            s = String(s)

        if self.data.max_length < len(self) + addlen + 1:
            dest = String(max_length=max(len(self) + addlen + 1,self.data.max_length))
            dest.copy(self)

        if isinstance(s, int):
            dest.data[len(self)] = s
            dest.data[len(self) + 1] = ord('\0')
        else:
            dest.data[len(self):len(self)+addlen] = s.data[:addlen]
            dest.data[len(self) + addlen] = ord('\0')

        dest.length = len(self)+addlen
        self.data = dest.data
        self.length = dest.length
        self = dest

        return self

    def find(self, token):
        res = List()
        cmplen = len(token)
        for i in range(0, len(self)-cmplen+1):
            if self.data[i:i+cmplen] == token.data[:token.length]:
                res.append(i)
        return res

    def split(self, token):
        res = List()
        buffer=String()
        cmplen = len(token)

        i=0
        while i < len(self):

            if i <= len(self)-cmplen and self.data[i:i+cmplen] == token.data[:token.length]:
                if len(buffer) > 0:
                    res.append(buffer)
                    buffer = String()
                i += token.length
            else:
                buffer.concatenate(self.data[i])
                i += 1

        if len(buffer)>0:
            res.append(buffer)

        return res

    def __add__(self, s):

        addlen = 1 if isinstance(s, int) else len(s)

        if isinstance(s, str) and len(s) > 1:
            s = String(s)

        dest = String(max_length=max(len(self) + addlen + 1,self.data.max_length))
        dest.copy(self)

        if isinstance(s, int):
            dest.data[len(self)] = s
            dest.data[len(self) + 1] = ord('\0')
        else:
            dest.data[len(self):len(self) + addlen] = s.data[:addlen]
            dest.data[len(self) + addlen] = ord('\0')

        dest.length = len(self) + addlen
        return dest


String.LOWER_BASE = ord('a')
String.UPPER_BASE = ord('A')
String.LOWER_END = ord('z')
String.UPPER_END = ord('Z')
String.UPPER_OFFSET = String.UPPER_BASE - String.LOWER_BASE

if __name__ == '__main__':
    s = String('hello world!')

    s.print()
    s.upper().print(prefix='To upper:')
    s.lower().print(prefix='To lower:')

    print(len(s))
    print(s[2:4])
    s[2:4] = 'ab'
    s.print(prefix='after slicing:')

    s.copy(String('this is a test'))
    s.print('after copy: ')

    a = String('123213.123')
    b = String('12a')
    print('a is numeric?:', a.isnumeric())
    print('b is numeric?:', b.isnumeric())

    s = String('')
    s.print()
    print(String('') == String(''))
    print(String('abc') == String('abc'))
    print(String('ab') == String('abc'))
    print(String('abcd') == String('abcc'))
    print(String('abcd') == String('abce'))

    a.print('a:')
    s = a.concatenate(String('hjk\n'))
    a.print('a:')

    s = a.concatenate(b)
    a.print('a:')

    #s.data.print()
    s.print()
    print(s.find(String('123')))
    print(s.split(String('13')))
    c=b+b
    print(c)