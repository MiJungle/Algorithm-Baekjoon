#소스: https://leetcode.com/problems/merge-intervals/submissions/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x:x[0])
        ans = []
        for i in intervals:
            newInterval = i
            #compare with the last one in ans
            if ans:
                if ans[-1][1] >= i[0]: 
                    #merge and then replace the last one in ans
                    newInterval = ans.pop()
                    if i[1] > newInterval[1]:
                        newInterval[1] = i[1]      
            ans.append(newInterval)
        return ans