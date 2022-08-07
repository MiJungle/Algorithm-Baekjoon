
#min max 때문에 효율성 테스트가 통과 안됐음
scoville = [0,3]
K = 6
import heapq

def solution(scoville, K):
    count = 0    
    arr = []
    heapq.heapify(scoville)
 
    while scoville[0]<K and len(scoville)!= 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        count +=1
    if len(scoville) == 1 and scoville[0]<K:
        return -1
    else:
        return count

print(solution(scoville,K))