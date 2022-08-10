clothes= [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
from collections import defaultdict;
def solution(clothes):
    arr = defaultdict(int)

    for i in clothes:
        arr[i[1]] +=1
    
    answer = 1
    for key,value in arr.items():
        answer *= (value+1)
    return answer -1
   
    
print(solution(clothes))