from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

v,e = map(int,input().split()) #노드 간선
indegree = [0]*(v+1) #노드에 대한 진입차수 0 
graph = [[]for _ in range (v+1)] # 각 노드에 연결된 간선 정보 담음

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) #정점 a -> b
    indegree[b] += 1 #b를 향하는 간선이 있다는 것이니까 b에다가 추가

def height():
    q = deque() #노드에 대한 진입차수 0 인 애들 차례로 담을 큐
    answer = [] #답을 담을 리스트

    for i in range(1, v+1):
        if indegree[i] == 0: 
            q.append(i)
    while q:           
        n = q.popleft()
        answer.append(n) #노드에 대한 진입차수 0 인애들이니까 answer 에 추가
        for i in graph[n]:
            indegree[i] -= 1 #간선을 빼주는 것
            if indegree[i] ==0: #노드에 대한 진입차수 확인
                q.append(i)

    return answer
print(*height(), end='')