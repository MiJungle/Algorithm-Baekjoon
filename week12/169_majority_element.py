import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) //2
        arr = collections.Counter(nums)
        
        for key, value in arr.items():
            if value > n:
                return key