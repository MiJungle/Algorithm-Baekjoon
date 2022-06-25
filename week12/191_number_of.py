class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

# Runtime: 11 ms, faster than 99.16% of Python online submissions for Number of 1 Bits.
# Memory Usage: 13.5 MB, less than 35.14% of Python online submissions for Number of 1 Bits.