arr = [4,3,2,1]	

def solution(arr):
    if len(arr) ==1:
        return -1
    n = min(arr)
    arr.remove(n)
    return arr

print(solution(arr))