
import sys
input=sys.stdin.readline
# 첫째 줄에 도시의 수 N이 주어진다.
# 한 번 갔던 도시는 갈 수 없음
# 가장 적은 비용을 들이는 여행 계획
# N개의 줄에는 비용 행렬이 주어진다.
# 갈 수 없는 경우는 0이 주어진다.
# 항상 순회할 수 있는 경우만 입력
n = int(input())
travelCost = [list(map(int, input().split())) for i in range(n)]
#[[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
minCost = sys.maxsize #출력할 최소값 정의
def dfsBack(start, next, cost, visited): #시작도시,다음도시,비용,방문도시
    global minCost #이걸 전역으로 안 빼면 지역변수가 되어서 계속해서 변수를 적어야함..즉 굉장히 귀찮
    if len(visited) == n: #방문 도시가 == n(4번 = 마지막도시)과 같아지면
        if travelCost[next][start] != 0: # 마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면 >> 갈 수 있다.
            minCost = min(minCost,cost+travelCost[next][start]) #비용+여행비용을 합쳐 최소값과 비교해 대입
        return
    for i in range(n):
        if travelCost[next][i] != 0 and i not in visited and cost < minCost:
        #현재>다음도시 넘어가는 비용이 0 이 아니고 방문한 적이 없으며 비용이 최소값보다 작다면~
            visited.append(i) #방문이 가넝하니까 방문한 곳에 추가
            dfsBack(start, i, cost+travelCost[next][i],visited) # 다음 도시를 가는 재귀함수
            visited.pop() #방문 했으면 방문한 도시 꺼내오고, 목록에서 삭제 진행
for i in range(n): #도시 출발점 지정!!!
    dfsBack(i,i,0,[i])
print(minCost)