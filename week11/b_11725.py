import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(input()) 
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
ans = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(k):
    visited[k] = 1
    for i in graph[k]:
        if visited[i] != 1:
            ans[i].append(k)
            dfs(i)
    return
dfs(1)
for i in range(2,len(ans)):
    print(ans[i][0])