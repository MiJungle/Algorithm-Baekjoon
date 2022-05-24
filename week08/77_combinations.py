from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        li = []
        for i in range(1,n+1):
            li.append(i)

        ans = list(combinations(li, k))
        fin = []
        for i in ans:
            k = list(i) 
            fin.append(k)
        return fin