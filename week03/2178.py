# 소스: https://jokerldg.github.io/algorithm/2021/03/24/maze.html

import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

def bfs(x,y): #미로는 BFS다 
    dx = [-1, 1, 0, 0] #행열에서 위아래로 움직였을때 
    dy = [0, 0, -1, 1]

# deque 생성
    queue = deque()
    queue.append((x,y)) #(0,0)

    while queue:
        x, y = queue.popleft()  #(0,0) #(1,0)추가

        for i in range(4):
            nx = x + dx[i]  #(-1) #(1) #(0) #0
            ny = y + dy[i] #(0) (0) #(-1) #1

            if nx < 0 or nx >= N or ny < 0 or ny>=M:
                continue #밑에 무시하고 다시 포문으로 돌린다
            if graph[nx][ny] == 0: # (1,0)
                continue

            if graph[nx][ny] == 1: ##숫자가 커지니까 여기서 걸러지기 떄문에 방문 탐색을 안해도 되는 것
                graph[nx][ny] = graph[x][y] + 1 #graph[0][0]= 1 + 1 = 2
                queue.append((nx, ny))
                print(nx,ny,  graph[nx][ny])
    return graph[N-1][M-1]
print(bfs(0,0))
#왜 BFS 문제인가?????
#초기값 (1,1) 을 visit [] 에 넣는다
#queue 에도 좌표를 넣는다
#큐가 있다면
#큐에서 좌표를 팝
#만약 그 수가 visited0 이고 좌표 자체가 = 1인 경우
#그 좌표를 append한다. 
#count를 출력한다.
#최소 경로인지는 어떻게 확인하는가? 

