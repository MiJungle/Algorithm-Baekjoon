import sys
import heapq

from sympy import N
sys.stdin = open('input.txt')

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting = sorted(meeting, key = lambda x: (x[1],x[0]))
#  (2,2) 와 (1,2) 있을 때 끝나는 시간으로 정렬을 한다면 (2,2)가 먼저 정렬되고 (1,2)가 무시된다. 그래서 시작과 끝 시간이 같은 경우는 시작 시간 기준으로 다시 정렬을 해줘야 한다.

ans = [meeting[0]]

def meet():
    global n
    if n <=1 :
        return 1
    
    else:
        for i in range(1, len(meeting)):
            if ans[-1][1] <= meeting[i][0]:
                heapq.heappush(ans, meeting[i])
    
    return(len(ans))

print(meet())