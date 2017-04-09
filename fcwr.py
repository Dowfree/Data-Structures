def fcwr():
    a = [0]*100
    for i in range(100):
        for j in range(i, 100):
            if (j+1) % (i+1) == 0:
                a[j] = a[j] + 1
    num = []
    for i in range(len(a)):
        if a[i] % 2 != 0:
            num.append(i+1)
    return num