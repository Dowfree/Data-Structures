import math
from Array import *
from Graph import *
# 冲突检查，在定义state时，采用state来标志每个皇后的位置，其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，则说明有冲突，需要重新摆放
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。


def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 产生当前皇后的位置信息
            if len(state) == num-1:
                yield (pos, )
            # 否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            else:
                for result in queens(num, state+(pos,)):
                    yield (pos, ) + result


# 为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

# 找出权值之后最大的图
A, weight = [], []
for i in range(8):
    A.append([math.inf]*8)
for node in list(queens(8)):
    for i in range(8):
        for j in range(i + 1, 8):
            tmp = 2
            for k in range(i + 1, j):
                if node[k] in range(node[i], node[j] + 1) or node[k] in range(node[j], node[i] + 1):
                    tmp += 1
            A[i][j] = tmp ** abs(int((i + j) / 2))
            A[j][i] = tmp ** abs(int((i + j) / 2))
    graph = UndirectedGraph(A, '01234567', True)
    sum_line = 0
    for line in graph.prim():
        sum_line += line[2]
    weight.append((sum_line, node))
weight.sort(reverse=True)
print(weight)

# 对该图输出结果
node = (3, 6, 2, 7, 1, 4, 0, 5)
for i in range(8):
    for j in range(i + 1, 8):
        tmp = 2
        for k in range(i + 1, j):
            if node[k] in range(node[i], node[j] + 1) or node[k] in range(node[j], node[i] + 1):
                tmp += 1
        A[i][j] = tmp ** abs(int((i + j) / 2))
        A[j][i] = tmp ** abs(int((i + j) / 2))
graph = UndirectedGraph(A, '01234567', True)
print((list(node), graph.prim(), 66))
