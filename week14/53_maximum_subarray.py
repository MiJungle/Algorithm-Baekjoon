class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        if len(nums) <= 1:
            return nums[0]
        else:
            if nums[0] <0:
                arr.append(0)
            else:
                arr.append(nums[0])

            for i in range(1, len(nums)):
                k = arr[-1]
                if k + nums[i] <=0:
                    arr.append(0)
                else:
                    arr.append(k+nums[i])
            if max(arr) == 0:
                return max(nums)
            else:
                return max(arr)