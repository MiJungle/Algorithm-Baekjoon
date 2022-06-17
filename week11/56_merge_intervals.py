import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
intervals = [[1,3],[2,6],[8,10],[15,18]]


"""
:type intervals: List[List[int]]
:rtype: List[List[int]]
"""
intervals.sort()
temp = []
ans = []
while intervals:
    temp.append(intervals.pop(0))
    if  intervals:
        if temp[-1][1]>= intervals[0][0]:
            temp.append([temp[-1][0],intervals[0][1]])
            temp.pop(-1)
            ans.append([temp[-1][0],intervals[0][1]])
        else:
            ans.append(intervals[0])
print(temp)
print(ans)

    # print(temp[-1][1],intervals[0][0])
    # if temp[-1][1]>= intervals[0][0]:
    #     print(temp)
    #     temp.append([temp[-1][0],intervals[0][1]])
    #     ans.append([temp[-1][0],intervals[0][1]])
    # else:
    #     temp.append(intervals[0])
    #     ans.append(intervals[0])

