class Solution(object):
    @staticmethod
    def to_swap(n1, n2):
        return str(n1) + str(n2) < str(n2) < str(n1)
    
    def largestNumber(self, nums):
        i = 1
        while i < len(nums):
            j = i
            while j >0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        return str(int(''.join(map(str, nums))))

#https://likevvs.tistory.com/22
class Solution:
    def swap(self, n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
    
    def largestNumber(self, nums):
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if self.swap(nums[j-1], nums[j]):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        
        return str(int(''.join(map(str, nums))))