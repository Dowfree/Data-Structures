# -*- coding:utf-8 -*-
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
re_path = []

"""迷宫解决问题的递归实现"""

def mark(maze, start):
    maze[start[0]][start[1]] = 2


def passable(maze, start):
    if 0 <= start[0] < len(maze) and 0 <= start[1] < len(maze[0]):
        return maze[start[0]][start[1]] == 0
    else:
        return False


def find_path(maze, start, end):
    mark(maze, start)
    if start == end:
        re_path.append(start)
        return True
    for i in range(4):
        nextp = (start[0]+dirs[i][0], start[1]+dirs[i][1])
        if passable(maze, nextp):
            if find_path(maze, nextp, end):
                re_path.append(start)
                return True
    return False


def maze_slover(maze, start, end):
    find_path(maze, start, end)
    re_path.reverse()
    path = re_path.copy()
    re_path.clear()
    return path

b = [[1, 0, 0, 0, 1], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]]
print(maze_slover(b, (1, 0), (3, 3)))
b = [[0, 0], [1, 0]]
print(maze_slover(b, (0, 0), (1, 1)))
