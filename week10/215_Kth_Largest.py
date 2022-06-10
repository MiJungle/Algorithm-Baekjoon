import heapq as hq
class Solution(object):
    def findKthLargest(self, nums, k):
        new = []
        hq.heapify(nums)
        for num in nums:
            hq.heappush(new,(-num,num))

        for _ in range(k-1):
            hq.heappop(new)

        return hq.heappop(new)[1]