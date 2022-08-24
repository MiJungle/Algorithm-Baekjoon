

arr = [1]
def solution(arr):
    ans = []
    print(len(ans),arr[0])
    for i in range(len(arr)):
        if len(ans)== 0:
            ans.append(arr[i])
        else:
            if arr[i] == ans[-1]:
                continue
            else:
                ans.append(arr[i])
    return ans

print(solution(arr))
