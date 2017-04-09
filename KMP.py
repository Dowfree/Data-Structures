from List import *
from String import String


def kmp(string, pattern, next):
    i = 0
    j = 0
    while i < len(string) and j < len(pattern):
        if j == -1 or string[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len(pattern):
        return i - j

    return -1


def getnext(pattern):
    next = List([0] * len(pattern))
    next[0] = -1
    count = 0
    for i in range(2, len(pattern)):
        for j in range(1,i):
            #print(i, j, pattern[:j], pattern[:i][-j:])
            if pattern[:j] == pattern[:i][-j:]:
                next[i] = j
            count += 1
    print('count 1:', count)
    return next


def getnext_dp(pattern):
    next = List([0] * len(pattern))
    next[0] = -1
    count = 0
    i = -1
    j = 0
    while j<len(pattern)-1:
        if i==-1 or pattern[i] == pattern[j]:
            i+=1
            j+=1
            next[j] = i
        else:
            i=next[i]
        count += 1
    print('count 2:', count)
    return next


s = String("ADABDACDBABCABDABCDABDABCADBCDD")
p = String("ABCDABD")
next = getnext(p)
print(next)
print(kmp(s, p, next))

s = String("AAADAAAAA")
p = String("AAAA")
next = getnext(p)
print(next)
print(kmp(s, p, next))

s = String("ADABDACDBABCABDABCDABDABCADBCDD")
p = String("ABCDABD")
next = getnext_dp(p)
print(next)
print(kmp(s, p, next))

s = String("AAADAAAAA")
p = String("AAAA")
next = getnext_dp(p)
print(next)
print(kmp(s, p, next))
