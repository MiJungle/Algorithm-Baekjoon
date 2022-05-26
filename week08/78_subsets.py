nums = [1,2,3]
#
ans = []

class Solution(object):
    def subsets(self, nums):
        ans = []
        def dfs(index, path):
            ans.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+ [nums[i]])
        dfs(0,[])
        return ans
print(Solution().subsets(nums))




















