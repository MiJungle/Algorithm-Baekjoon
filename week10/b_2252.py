from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

v,e = map(int,input().split())
indegree = [0]*(v+1)
graph = [[]for _ in range (v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
print(graph)
print(indegree)

def height():
    q = deque()
    answer = []

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:           
        n = q.popleft()
        answer.append(n)
        for i in graph[n]:
            indegree[i] -= 1
            if indegree[i] ==0:
                q.append(i)

    return answer
print(*height(), end='')