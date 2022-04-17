from platform import java_ver
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int,input().split())
visited = [[0] *(n+1) for _ in range(n)]
m = []
for _ in range(n):
    m.append(list(map(int, input().split())))
print(m)

def bfs(i,j):
    visited[i][j] = 1
    queue=[(i,j)]
    while queue:
        v = queue.pop(0)
        print(v, end =' ')
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and m[v] [i] == 1:
                    queue.append(i)
                    visited[i] = 1