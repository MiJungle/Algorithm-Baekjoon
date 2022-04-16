# 소스: https://pacific-ocean.tistory.com/260

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n,m,v = map(int,input().split())
s = [[0] *(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

def dfs(v): ##재귀 방법
    visit[v]=1 #visited에 시작 정점 입력- 1이면 visited를 의미함 
    print(v, end=' ') #정점 출력
    for i in range(1, n+1): #정점의 개수만큼 반복
        if (visit[i]==0 and s[v][i]==1): #visited 하지 않은 것 중에서 방문할 것이 있으면 
            dfs(i)

def bfs(v):
    visit[v] = 0
    queue= [v]
    while queue: 
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0 #앞선 dfs에서 1로 처리해줬기 때문에 0으로 visited 표시
dfs(v)
print()
bfs(v)
print()