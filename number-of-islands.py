# coding=utf8

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution(object):
    @classmethod
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid[0]) == 0:
            return 0

        def rebuild(grid):
            m = len(grid)
            n = len(grid[0])
            row = [0] * n
            rs = []
            for i in range(m):
                rs.append(list(row))

            for i in range(m):
                for j in range(n):
                    rs[i][j] = int(grid[i][j])
            return rs


        grid = rebuild(grid)

        m = len(grid)
        n = len(grid[0])
        island_num = 0

        for i in range(m):
            for j in range(n):
                if int(grid[i][j]) == 1:
                    self.mark_by_bfs(grid, i, j)
                    island_num += 1
        return island_num
    @classmethod
    def mark_by_bfs(self, grid, i, j):
        queue = [[i, j]]
        grid[i][j] = 0
        coor_xy = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while queue:
            _x, _y = queue[0]
            queue.remove([_x, _y])
            for coor_x, coor_y in coor_xy:
                new_x, new_y = _x + coor_x, _y + coor_y
                if not self.inbound(grid, new_x, new_y):
                    continue
                if int(grid[new_x][new_y]) == 1:
                    grid[new_x][new_y] = 0
                    queue.append([new_x, new_y])

    @classmethod
    def inbound(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        return x >= 0 and x < m and y >= 0 and y < n


if __name__ == '__main__':
    f = Solution.numIslands
    input = ["11000","11000","00100","00011"]  #  leetcode 的输入是字符串

    print f(input)
