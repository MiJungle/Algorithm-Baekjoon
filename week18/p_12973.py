s= "bbbbb"

def solution(s):
    s= list(s)
    left = 0
    right = left + 1
    while right <= len(s)-1: 
        if s[left] == s[right]:
            s.remove(s[left])
            s.remove(s[left])
            left = 0 
            right = left + 1

        else:
            left += 1
            right = left + 1
    if len(s) == 0:
        return 1
    else:
        return 0

print(solution(s))



