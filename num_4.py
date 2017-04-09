guts = open("try.txt").read()
a = []
j = 0
k = 1
for i in range(len(guts)):
    if guts[i] != ' ' and guts[i] != '\n':
        a.append(guts[i])
for i in range(len(a)):
    if i == j:
        a[i] = a[i].upper()
        k += 1
        j += k
a.reverse()
print(''.join(a))


