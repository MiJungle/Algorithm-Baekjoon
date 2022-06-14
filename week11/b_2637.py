import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[b].append((a,c))
    indegree[b] += 1
print(indegree)
print(graph)

``