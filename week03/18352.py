#  소스: https://velog.io/@kimdukbae/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Dijkstra-Algorithm
import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
Inf= int(1e9)

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)] #정점과, 가중치를 담는 곳(1)
distance = [[Inf] * (n+1)] #거리를 담는 곳

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) #dist = 0 now = 1
        # --> 꺼낸 노드 = 현재 최소 비용을 갖는 노드
        # 해당 노드의 비용이 현재 distance 배열에 기록된 비용보다 크다면 최단 경로가 아니기 때문에 무시해도 상관 X
            #distance[now] 는 cost, dist는 cost
            #이미 담겨져있는 값이 dist- 계속 더해져 온cost 보다 작으면 업데이트 할 필요 없음 
        if distance[now] < dist:  #distance[1]= 0 < 0, 굳이 비교안해도 되는 것 
            continue 
        for j in graph[now]: #(2,1), (3,1) 인접노드 확인    
            cost = dist + j[1] # 가중치 1더하기(거리) 1 , 1
            if cost < distance[j[0]]: 
                distance[j[0]] = cost #cost 로 업데이트된다 
                heapq.heappush(q, (cost, j[0])) #(1, 2)

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k: 
        answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')
