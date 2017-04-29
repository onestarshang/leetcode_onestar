# coding=utf8

'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    @classmethod
    def divide(self, dividend, divisor):
        # Write your code here
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1

        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans

if __name__ == '__main__':
    f = Solution.divide
    f(100, 9)
