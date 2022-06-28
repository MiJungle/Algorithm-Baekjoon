import heapq
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1]>0 else 0
        return max(nums)
            
            


##시간 초과, 209개 중 9개 test case 통과 못함
import heapq
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        posidx = []
        ans = []
        for i in range(len(nums)):
            if nums[i]>0:
                posidx.append(i) #index를 담아
                ans.append(nums[i]) #자기 자신 숫자들도 담아
                
        if len(posidx) == 0:
            return max(nums) #모두 음수라는 의미니까 음수 중 가장 큰거 고름
    
        elif len(posidx) == 1:
            return nums[posidx[0]] #양수 1개라는 것이니까 그 숫자 자체 출력
        
        big = max(ans)
        while posidx:
            a = heapq.heappop(posidx)
            for i in posidx:
                sums = sum(nums[a:i+1])
                if sums > big:
                    big = sums

        return(big)

