










# 시간초과

# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         ans = []
#         for i in range(0, len(nums)-k+1):
#             ans.append(max(nums[i:i+k]))
        
#         return ans