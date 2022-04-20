
   
# 소스: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2665%EB%B2%88-%EB%AF%B8%EB%A1%9C%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://rebas.kr/756

from collections import deque

n = int(input())
a = [list(input().strip()) for _ in range(n)]
dist = [[-1]*n for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0))
    dist[0][0] = 0
    while q:
        x, y = q.pop()
        if x == n-1 and y == n-1:
            print(dist[x][y])
            return
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] == -1:
                if a[nx][ny] == '1':
                    dist[nx][ny] = dist[x][y]
                    q.append((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y]+1
                    q.appendleft((nx, ny))

bfs()


출처: https://rebas.kr/756 [PROJECT REBAS]