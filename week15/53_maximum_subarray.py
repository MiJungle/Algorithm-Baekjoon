class Solution(object):
    def maxSubArray(self, nums):

        new = [nums[0]]
        for i in range(1,len(nums)):
                new.append(max(nums[i], new[-1]+nums[i]))
                
        return max(new)