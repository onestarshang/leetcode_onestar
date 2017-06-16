# coding=utf8

'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph
at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`,
check if two nodes are connected

Have you met this question in a real interview? Yes
Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
'''

class ConnectingGraph:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.father = [i for i in range(n + 1)]

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b
