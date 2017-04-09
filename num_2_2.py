# -*- coding: utf-8 -*-
import numpy as np
a = np.zeros((25, 5))
a[0,4] = 1
for i in range(1, 25):
    a[i, 0] = a[i-1, 1]
    a[i, 1] = a[i-1, 2]
    a[i, 2] = a[i-1, 3]
    a[i, 3] = a[i-1, 4]
    a[i, 4] = a[i, 0] + 3*a[i, 1] + 2*a[i, 2]
tuzi = a[24, 0] + a[24, 1] + a[24, 2] + a[24, 3] + a[24, 4]
print(int(2*tuzi))
