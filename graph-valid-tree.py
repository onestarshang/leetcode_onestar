# coding=utf8

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
    edge is a pair of nodes), write a function to check whether these edges
make up a valid tree.

 Notice

You can assume that no duplicate edges will appear in edges. Since all edges
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if n == 0 or n is None:
            return False
        if len(edges) != n - 1:
            return False

        graph = self.init_graph(n, edges)
        queue = [0]
        hash = set([0])
        while queue:
            node = queue[0]
            queue.remove(node)
            for neighbor in graph.get(node):
                if neighbor in hash:
                    continue
                hash.add(neighbor)
                queue.append(neighbor)
        return len(hash) == n

    def init_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = set()

        for edge in edges:
            u, v = edge[0], edge[1]
            graph.get(u).add(v)
            graph.get(v).add(u)
        return graph
