# coding=utf8

'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have
finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency
matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = self.node_degree(numCourses, prerequisites)
        graph = self.init_graph(numCourses, prerequisites)

        queue = []
        for n, degree in degrees.items():
            if degree == 0:
                queue.append(n)
        cnt = 0
        while queue:
            course = queue[0]
            queue.remove(course)
            cnt += 1
            n = len(graph.get(course))
            for i in range(n):
                pointer = graph.get(course)[i]
                degrees[pointer] -= 1
                if degrees[pointer] == 0:
                    queue.append(pointer)
        return cnt == numCourses


    def node_degree(self, numCourses, prerequisites):
        degrees = {i: 0 for i in range(numCourses)}
        for n, _ in prerequisites:
            degrees[n] += 1
        return degrees

    def init_graph(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for n, v in prerequisites:
            graph.get(v).append(n)
        return graph
