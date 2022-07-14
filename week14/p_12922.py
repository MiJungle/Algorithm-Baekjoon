def solution(n):
    ans = []
    for i in range(n):
        if i %2 == 0:
            ans.append("수")
        else:
            ans.append("박")
    ans = "".join(ans)
    return ans