s="AB"
n =1
def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz"
    high = low.upper()
    arr = []
    for i in s:
        if i in low:
            ans = low[(low.index(i) +n)%26]
        elif i in high:
            ans = high[(high.index(i) +n)%26]
        else:
            ans = " "
        arr.append(ans)
    arr= "".join(arr)
    return arr