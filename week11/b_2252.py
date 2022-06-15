import sys
from collections import deque as dq
sys.stdin = open('input.txt')
input = sys.stdin.readline

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def height():
    q = dq()
    ans = []
    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    while q:
        num = q.popleft()
        ans.append(num)

        for i in graph[num]:
            indegree[i]-= 1
            if indegree[i] ==0:
                q.append(i)
    return ans
print(*height())
