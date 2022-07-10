import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
intervals = [[1,3],[2,6],[8,10],[15,18]]


"""
:type intervals: List[List[int]]
:rtype: List[List[int]]
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        if intervals:
            temp = [intervals[0]]
        ans = []

        for i in range(1, len(intervals)):
            if temp[-1][1]>= intervals[i][0]:
                k = temp.pop()
                temp.append([k[0], max(intervals[i][1], k[1])])
                             
            else:
                temp.append(intervals[i])

        return temp

# Runtime: 117 ms, faster than 89.37% of Python online submissions for Merge Intervals.
# Memory Usage: 18.2 MB, less than 72.36% of Python online submissions for Merge Intervals.