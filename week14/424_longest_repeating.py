s = "ABAB"
k = 2
Output: 4

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d= {}
        i = 0
        ans = 0
        for j in range(len(s)):
            d[s[j]]= d.get(s[j],0) +1
            cnt = j-i+1 - max(d.values())
            while cnt > k:
                d[s[i]]-= 1
                i+= 1
                cnt = j-i+1 -max(d.values())
            ans = max(j-i+1, ans)
        return ans

# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         d = {}
#         ans =0        
#         i = 0
#         for j in range(len(s)):
#             d[s[j]] = d.get(s[j],0) +1
#             cnt = j-i + 1 - max(d.values())
#             while cnt > k:
#                 d[s[i]] -= 1
#                 i += 1
#                 cnt = j-i+ 1 - max(d.values())
#             ans = max(j-i+1, ans)
#         return ans