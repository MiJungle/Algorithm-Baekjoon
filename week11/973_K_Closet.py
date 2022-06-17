class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in points:
            num = (i[0]**2 + i[1]**2)**0.5
            ans.append([num, i])
        ans.sort()
        
        fin= []
        for i in range(k):
            fin.append(ans[i][1])
        return fin
