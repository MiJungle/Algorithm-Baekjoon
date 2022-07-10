#간단 풀이
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         ans = []
#         nums1 = set(nums1)
#         nums2 = set(nums2)
#         for i in nums1:
#             for j in nums2:
#                 if i ==j:
#                     ans.append(i)
#         return ans

# Runtime: 128 ms, faster than 5.15% of Python online submissions for Intersection of Two Arrays.
# Memory Usage: 13.6 MB, less than 60.97% of Python online submissions for Intersection of Two Arrays.