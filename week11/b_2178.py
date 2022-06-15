#최소 경로 보장???
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q = [(0,0)]

    while q:
        a, b = q.pop(0)

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx <0 or nx>=n or ny <0 or ny >=m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] +1
                q.append((nx,ny))
    print(graph)
    return graph[n-1][m-1]

print(bfs())

