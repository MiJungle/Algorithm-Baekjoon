import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N,M = map(int, input().split())
visited =[0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    visited[n] = 1
    print(n,end=' ')
    for i in graph[n]:
        if visited[i] != 1:
            dfs(i)


# count = 0
# def solution():
#     global count
#     for i in range(1,N+1):
#         if visited[i] == 0:
#             dfs(i)
#             count += 1
#     return count
# print(solution())
