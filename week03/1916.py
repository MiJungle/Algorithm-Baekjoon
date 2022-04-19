# 소스:https://pacific-ocean.tistory.com/283

import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
Inf = 1e9

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [Inf] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end =map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = j[1] + dist
            if cost < distance[j[0]]:
                distance[j[0]]= cost
                heapq.heappush(q, (cost,j[0]))


dijkstra(start)
print(distance[end])
