# coding=utf8

'''
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

## quick select

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return -1

        return self.quick_select(nums, 0, len(nums)-1, k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left, right = start, end
        mid = (start + end) /2
        pivot = nums[mid]

        while left <= right:
            while left <= right and nums[left] > pivot:   # 大的数排在前面
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1                                # right --
            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1

        if start + k -1 <= right:
            return self.quick_select(nums, start, right, k)
        if start + k -1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right + 1]
