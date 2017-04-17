# coding=utf8
'''
An image is represented by a binary matrix with 0 as a white pixel and 1
as a black pixel. The black pixels are connected, i.e., there is only
one black region. Pixels are connected horizontally and vertically.
Given the location (x, y) of one of the black pixels, return the area
of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
'''


class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        h = len(image)      #  高
        w = len(image[0])   #  宽

        left = self.find_left(image, 0, y)
        right = self.find_right(image, y, w-1)
        top = self.find_top(image, 0, x)
        bottom = self.find_bottom(image, x, h-1)

        return (right - left + 1) * (bottom - top + 1)

    def find_left(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.empty_column(image, mid):
                start = mid
            else:
                end = mid
        if self.empty_column(image, start):   # 检验start
            return end
        return start

    def find_right(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.empty_column(image, mid):
                end = mid
            else:
                start = mid
        if self.empty_column(image, end):    # 检验 end
            return start
        return end

    def find_top(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.empty_row(image, mid):
                start = mid
            else:
                end = mid
        if self.empty_row(image, start):   # 检验 start
            return end
        return start

    def find_bottom(self, image, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.empty_row(image, mid):
                end = mid
            else:
                start = mid
        if self.empty_row(image, end):    # 检验 end
            return start
        return end


    def empty_column(self, image, col):  # 某一列是否有 1
        for i in range(len(image)):
            if image[i][col] == '1':
                return False
        return True

    def empty_row(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == '1':
                return False
        return True
