class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result

# 쉬운 풀이
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for i in nums:
#             if nums.count(i)!=2:
#                 return i

# Runtime: 7056 ms, faster than 5.01% of Python online submissions for Single Number.
# Memory Usage: 15.5 MB, less than 90.29% of Python online submissions for Single Number.