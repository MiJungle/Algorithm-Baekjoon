# 소스: https://hillier.tistory.com/46
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n,m = map(int, input().split())
s = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    s[x][y] = s[y][x] = 1

def dfs(v):
    visited[v] = 1
    for i in range(1,n+1):
        if visited[i] == 0 and s[v][i] ==1:
            dfs(i)

count = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        count+=1
print(count)