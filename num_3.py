from Queue import *
from Stack import *

jinru = List('K5H/?4]G>1Z(%JP8ND7VTQ0;F!<U^*{63A:_,)S9L.[WOMYEX@R}+I&#$=C2B')
shuchu = List('')
b = []
for i in range(len(a)):
    if a[i] == '+':
        b.append('-')
    elif a[i] == '-':
        b.append('+')
    else:
        b.append(a[i])
print(''.join(b))
