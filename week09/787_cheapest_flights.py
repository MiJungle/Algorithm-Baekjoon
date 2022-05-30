
import collections
import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w)) #인접경로 생성
        Q = [(0, src, k)] #도착지, 경유지 수
        
        while Q:
            price, node, k = heapq.heappop(Q) #초기값 (0,0,1)
            if node == dst: #도착지인 경우
                return price
            if k>= 0:
                for v, w in graph[node]: #도착지,cost
                    alt = price + w #최소비용 쌓아감 
                    heapq.heappush(Q,(alt, v, k-1)) #v에서부터 또 시작 (비용이 누적되고 갈 수 있는 경유지 줄어들음)
        return -1