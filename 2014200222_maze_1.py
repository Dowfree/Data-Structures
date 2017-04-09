from Stack import *

# -*- coding:utf-8 -*-
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

"""迷宫解决问题的栈实现"""

def mark(maze, start):
    maze[start[0]][start[1]] = 2


def passable(maze, start):
    if 0 <= start[0] < len(maze) and 0 <= start[1] < len(maze[0]):
        return maze[start[0]][start[1]] == 0
    else:
        return False


def print_path(path, start, nextp):
    new_path = [nextp, start]
    while not path.is_empty():
        new_path.append(path.pop()[0])
    new_path.reverse()
    return new_path


def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    path = Stack()
    mark(maze, start)
    path.push((start, 0))
    while not path.is_empty():
        start, direc = path.pop()
        for i in range(direc, 4):
            nextp = (start[0] + dirs[i][0], start[1]+dirs[i][1])
            if nextp == end:
                return print_path(path, start, nextp)
            if passable(maze, nextp):
                path.push((start, i+1))
                mark(maze, nextp)
                path.push((nextp, 0))
                break
    raise ValueError("No solution for the maze.")
