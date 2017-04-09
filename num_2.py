# -*- coding: utf-8 -*-
a = []
a.append(1)
for i in range(24):
    n = len(a)
    for j in range(n):
        a[j] += 1
        if a[j] == 3:
            a.append(1)
            a.append(1)
        if a[j] == 4:
            a.append(1)
            a.append(1)
            a.append(1)
        if a[j] == 5:
            a.append(1)
tuzi = 0
for i in range(len(a)):
    if a[i] < 6:
        tuzi += 1
print(tuzi*2)


