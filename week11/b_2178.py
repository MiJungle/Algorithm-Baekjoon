import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
graph = [[] for _ in range(n)]

dx= [-1,1,0,0]
dy = [0,0,-1,1]


def maze():
    dq = deque([[0,0]])
    while dq:
        a,b = dq.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if nx <0 or nx>= n or ny<0 or ny>=m:
                continue
            elif arr[nx][ny] == 1:
                arr[nx][ny] += arr[a][b]
                dq.append([nx, ny])         

    return arr[n-1][m-1]

print(maze())
