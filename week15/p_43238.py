# 시간초과
# 
# n =6
# times = [7, 10]	


# def solution(n, times):
#     arr = []
#     for i in range(1,n):
#         for time in times:
#             arr.append(time*i)
#     arr.sort()
#     return arr[n-1]


# print(solution(n,times))

def solution(n,times):
    answer = 0
    left = 1
    right = max(times)*n

    while left <= right:
        mid = (left+right)//2

        people = 0

        for time in times:
            people += mid// time
            if people >= n:
                break
        
        if people < n:
            left = mid + 1

        elif people >= n:
            answer = mid
            right = mid -1
    return answer