class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = [0,0,0,0,0]
        
        
        for i in range(len(nums)):
            while 2*i != len(nums):
                ans[0] += nums[2*i] if nums[2*i] else 0
                ans[1] += nums[2*i-1] if nums[2*i-1] else 0
                ans[2] += nums[3*i] if nums[3*i] else 0
                ans[3] += nums[3*i -1] if nums[3*i-1] else 0
                ans[4] += nums[3*i-2] if nums[3*i-2] else 0
        return max(ans)
            
        