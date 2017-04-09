# -*- coding:utf-8 -*-
guts = open("num_5.txt").read()

pos = []
for i in range(len(guts)-4):
    if guts[i:i+5].count('朱') == 1 and guts[i:i+5].count('未') == 1 and guts[i:i+5].count('末') == 1 and \
                    guts[i:i+5].count('失') == 1 and guts[i:i+5].count('夫') == 1:
        pos.append(i)
print(pos)

maxword = []
for i in range(len(guts)):
    for j in range(i+1, len(guts)):
        if guts[j] != guts[i]:
            if j-i > 4:
                maxword.append((guts[i], i, j-i))
            break
        else:
            continue

a = {'失': guts.count('失'), '朱': guts.count('朱'), '未': guts.count('未'), '末': guts.count('末'),
     '夫': guts.count('夫'), 'pos': pos, 'max': ('夫', 3657, 6)}
print(a)

