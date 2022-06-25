from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(t)
        li = defaultdict(list)
        for i in t:
            for j in range(len(s)):
                if i == s[j]:
                    li[i].append(j)
        arr = []
        for i in li:
            for j in range(len(i)):
                arr.append()