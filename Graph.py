from List import LiuDataStructure, List
from Array import Array2D
from String import String
import math
from Stack import Stack
from Queue import Queue
from queue import PriorityQueue
from math import isinf


class UndirectedGraph(LiuDataStructure):
    def __init__(self, data=[], labels=[], weighted=False):  # [[],[]..]
        self.graph = Array2D(data)
        self.labels = labels
        self.weighted = weighted
        self.n_vertex = len(data)

        if len(labels) > 0:
            self.labels = labels
        else:
            self.labels = List(range(1, 1 + len(data)))

    def __repr__(self):
        S = String('')
        if len(self.labels):
            S.concatenate(String('    '))
            for c in self.labels:
                if self.weighted:
                    S.concatenate(String('  %s   ' % c))
                else:
                    S.concatenate(String(' %s ' % c))
            S.concatenate(String('\n'))
        for i in range(self.graph.shape[0]):
            s = String(self.labels[i] + '  [' if len(self.labels) > 0 else ' [')
            for j in range(self.graph.shape[1]):
                if self.weighted:
                    s.concatenate(String(' %.2f ' % self.graph[i, j]))
                else:
                    s.concatenate(String(' %s ' % str(self.graph[i, j])))
            s.concatenate(String(']\n'))
            S.concatenate(s)

        return S.__repr__()

    def out_degree(self):
        od = List()
        for i in range(self.graph.shape[0]):
            row = self.graph[i].data
            od.append(sum(row))
        return od

    def in_degree(self):
        return self.out_degree()

    def traverse_breadth_first(self):
        visited = set()
        q = Queue([0])
        while len(visited) != self.graph.shape[0]:
            while not q.is_empty():
                node = q.dequeue()
                if node not in visited:
                    print('visiting %s' % str(self.labels[node]))
                    visited.add(node)

                for j in range(self.graph.shape[0]):
                    if node != j and self.graph[node, j] and j not in visited:
                        q.enqueue(j)

            next = 0
            while next in visited:
                next += 1
            if next < self.graph.shape[0]:
                print('new sub-graph')
                q.enqueue(next)

    def _traverse_depth_first_recur(self, i=-1, visited=None):
        if not visited[i]:
            print('visiting %s' % str(self.labels[i]))
            visited[i] = True

            for j in range(self.graph.shape[0]):
                if i != j and self.graph[i, j] and not visited[j]:
                    self._traverse_depth_first_recur(j, visited)

    def traverse_depth_first_recur(self):
        visited = List([False] * self.graph.shape[0])
        for i in range(self.graph.shape[0]):
            if not visited[i]:
                print('new sub-graph')
                self._traverse_depth_first_recur(i, visited)

    def traverse_depth_first(self):

        visited = set()
        s = Stack([0])
        while len(visited) != self.graph.shape[0]:
            while not s.is_empty():
                node = s.peek()

                if node not in visited:
                    print('visiting %s' % str(self.labels[node]))
                    visited.add(node)

                node_complete = True
                for j in range(self.graph.shape[0]):
                    if node != j and self.graph[node, j] and j not in visited:
                        s.push(j)
                        node_complete = False
                        break

                if node_complete:
                    node = s.pop()

            next = 0
            while next in visited:
                next += 1
            if next < self.graph.shape[0]:
                print('new sub-graph')
                s.push(next)

    def prim(self):
        if not self.weighted:
            raise TypeError('The Prim algorithm works with weighted graphs only')

        U, V = {0}, set(range(1, self.n_vertex))
        res = List()
        while len(U) != self.n_vertex:
            edge = None
            min_weight = math.inf

            for i in U:
                for j in V:
                    if not isinf(self.graph[i, j]) and self.graph[i, j] < min_weight:
                        edge = (i, j, self.graph[i, j])
                        min_weight = self.graph[i, j]

            a, b = (edge[0], edge[1]) if edge[0] < edge[1] else (edge[1], edge[0])
            res.append((self.labels[a], self.labels[b], edge[2]))
            print(U, V, edge)
            U.add(edge[1])
            V.remove(edge[1])

        return res

    def has_loop(self, vset):
        pass

    def kruskal(self):
        q = PriorityQueue()
        U = set()
        res = List()
        for i in range(self.n_vertex):
            for j in range(i+1):
                if not isinf(self.graph[i, j]):
                    q.put((self.graph[i, j], i, j))

        while not q.empty():
            weight, i, j = q.get_nowait()
            print(weight,i,j)
            tU = U.union([i,j])
            if not self.has_loop(tU):
                a, b = (i, j) if i < j else (j, i)
                res.append((self.labels[a], self.labels[b], weight))

        return res


# class Graph(LiuDataStructure):
#     def __init__(self, data=[], labels=[], undirected=True, weighted=False): #[[],[]..]
#         self.graph = Array2D(data)
#         self.labels = labels
#         self.undirected = undirected
#         self.weighted = weighted
#
#     def __repr__(self):
#         S = String('')
#         if len(self.labels):
#             S.concatenate(String('    '))
#             for c in self.labels:
#                 S.concatenate(String('  %s   '%c))
#             S.concatenate(String('\n'))
#         for i in range(self.graph.shape[0]):
#             s = String(self.labels[i]+'  [' if len(self.labels)>0 else ' [')
#             for j in range(self.graph.shape[1]):
#                 s.concatenate(String(' %.2f ' % self.graph[i, j]))
#             s.concatenate(String(']\n'))
#             S.concatenate(s)
#
#         return S.__repr__()
#
#     def out_degree(self):
#         od = List()
#         for i in range(self.graph.shape[0]):
#             row = self.graph[i].data
#             od.append(sum(row))
#         return od
#
#     def in_degree(self):
#         if self.undirected:
#             return self.out_degree()
#         else:
#             id = List()
#             for j in range(self.graph.shape[0]):
#                 id.append(sum([self.graph[i,j] for i in range(self.graph.shape[0])]))
#         return id
#
