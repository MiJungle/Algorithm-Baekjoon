n = 5 
lost=[2,3] 
reserve= [1,4]

def solution(n, lost, reserve):
        
    for i in lost:
        if i in reserve:
            reserve.remove(i)
    
    while reserve:
        leftover = reserve.pop()
        for i in range(len(lost)):
            if leftover - 1 in lost or leftover+1 in lost:
                lost.remove(leftover-1)
    answer = n - len(lost)

    return answer

print(solution(n,lost,reserve))