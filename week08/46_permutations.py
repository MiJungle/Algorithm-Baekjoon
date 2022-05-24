from itertools import permutations;

class Solution(object):
    def permute(self, nums):

        li = list(permutations(nums,len(nums)))
        ans = []
        for i in li:
            s = list(i)
            ans.append(s)
        return ans