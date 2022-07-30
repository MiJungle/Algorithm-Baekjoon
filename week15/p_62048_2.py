def gcn(w,h):
    a = max(w,h)
    b = min(w,h)
    while a:
        r = a % b
        if r== 0:
            return b
        else:
            a = b
            b = r

def solution(w,h):
    
    answer = w*h - (w+h-gcn(w,h))
    return answer