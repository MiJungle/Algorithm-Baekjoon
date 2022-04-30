import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
A = list(map(int,input().rstrip()))
graph = [[] for _ in range(N+1)]
visited = [0]* (N+1)

answer = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    if A[a-1] == 1 and A[b-1] == 1:
        answer +=2 #실내에서 실내를 더해줌 

def dfs(v, indoor): #실외에 둘러싸인 실내를 구함 
    visited[v] = 1
    for i in graph[v]:
        if A[i-1] == 1:
            indoor +=1 
        if visited[i] == 0 and A[i-1] == 0:
            indoor = dfs(i, indoor)
    return indoor

def solution():
    global answer
    for i in range (1, N+1):
        if visited[i] == 0 and A[i-1] == 0:
            n = dfs(i, 0)
            answer += n * (n-1) #(A-B , B-A 는 다른길이기 때문에 곱해줌)

solution()
print(answer)


# 초반 접근:
# 1번 정점에서 시작한다, visited에 1번을 넣어준다
# 인접 정점으로 간다 - 만약 그 값이 0 이면 visited 로 더해주고
# 1 인경우 산챌을 끝낸다. 
# dfs를 돌때마다 카운트를 세준다. 