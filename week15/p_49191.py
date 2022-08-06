
from collections import defaultdict
n= 5	
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	

def solution(n, results):
    
    arr = defaultdict(int)
    for i in results:
        for j in i:
            arr[j] += 1
    answer = 0
    
    if max(arr.values()) == n-1:
        answer+= 1

    num = []
    for key, v in enumerate(arr):
        if arr[v] == max(arr.values()):
            num.append(v)
    x
    left = 0
    right = 0

    for i in range(len(results)):
        if results[i][0] == num[0]:
            left += 1
        elif results[i][1] == num[0]:
            right += 1
    
    if left == 1 or right == 1:
        answer += 1
    return answer

print(solution(n, results))