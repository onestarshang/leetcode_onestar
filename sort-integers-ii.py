# coding=ut8

'''
给一组整数，按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
'''


## merge sort
## quick sort

class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        if not A:
            return

        temp = [0] * len(A)
        self.merge_sort(A, 0, len(A) -1, temp)

    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return

        self.merge_sort(A, start, (start+ end)/2, temp)
        self.merge_sort(A, (start + end)/2 + 1, end, temp)
        self.merge(A, start, end, temp)

    def merge(self, A, start, end, temp):

        if start >= end:
            return

        mid = (start + end) / 2
        left_index, right_index = start, mid + 1
        temp_index = start


        while left_index <= mid and right_index <= end:
            if A[left_index] <= A[right_index]:
                temp[temp_index] = A[left_index]
                left_index += 1
            else:
                temp[temp_index] = A[right_index]
                right_index += 1
            temp_index += 1

        while left_index <= mid:
            temp[temp_index] = A[left_index]
            temp_index += 1
            left_index += 1

        while right_index <= end:
            temp[temp_index] = A[right_index]
            temp_index += 1
            right_index += 1

        while start <= end:
            A[start] = temp[start]
            start += 1

    '''
        self.quick_sort(A, 0, len(A) - 1)

    def quick_sort(self, A, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = A[(start + end) / 2]

        while left<=right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp

                left += 1
                right -= 1

        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)
    '''
