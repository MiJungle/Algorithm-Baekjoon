import heapq
#Heap pop 하면 0번째 index값이 나오는 것이지 항상 작은게 나오는게 아님, 
# heapq로 정렬됐다는 가정하에 0번째가 출력되므로 그냥 array의. 경우에는 heapify를 해줘야함. 

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
def solution(operations):
    arr = []
    for i in operations:
        if i[0] == "I":
            a,b = i.split(" ")
            heapq.heappush(arr,int(b))
        elif i == "D -1" and arr:
            heapq.heapify(arr)
            heapq.heappop(arr)
        elif i == "D 1"  and arr:
            arr = [i*(-1) for i in arr]
            heapq.heapify(arr)
            heapq.heappop(arr)
            arr = [i*(-1) for i in arr]
    if len(arr) != 0:
        return([max(arr),min(arr)])
    else:
        return [0,0]

print(solution(operations))

# nums = [6, 99,18, 2]
# nums = [i*(-1) for i in nums]
# heapq.heapify(nums)

# print(nums)
# a = heapq.heappop(nums)
# print(a)
# print(nums)