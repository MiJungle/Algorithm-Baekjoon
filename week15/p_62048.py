def gcb(w,h):
    a,b = max(w,h), min(w,h)
    while True:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r
    
def solution(w,h):
    answer = w*h -(w + h - gcb(w,h))
    return answer