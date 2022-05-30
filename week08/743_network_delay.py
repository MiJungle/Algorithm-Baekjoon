import collections
import heapq
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

# dfs 0번쨰 index 인자 바탕으로 깊이우선 탐색 
# node를 방문할 때마다 2번째 index 값을 더해줌 
#visited 가 모두 1일 때 count값을 반환
class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w)) #인접경로 생성
        Q = [(0, k)] #소요시간, 정점
        dist = collections.defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q) #초기값 (0,k)
            if node not in dist:
                dist[node] = time #초기값 0 
                for v, w in graph[node]: #도착지, 소요시간
                    alt = time + w #소요시간 +0
                    heapq.heappush(Q,(alt, v)) #v에서부터 또 시작 (걸린 시간이 누적돼서 더해짐)
        
        if len(dist) == n: #모든 정점을 돌 수 있으면 출력
            return max(dist.values())
        return -1