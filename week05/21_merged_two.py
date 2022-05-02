list1 = [] 
list2 = [0]

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ans = list1 + list2
        ans.sort()
        return ans

print(Solution().mergeTwoLists(list1,list2))

