#index 오류남, 점화식 못찾음

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n  = int(input())
score = [int(input().rstrip()) for _ in range(n)]
score = [0] + score
ans = score[1] + score[-1]
A = score[2:-1]
def highscore(n):
    global ans
    if n == 0:
        return 0
    first = 0
    for i in range(len(A)//2):
        if len(A)% 2 != 0:
            ans += A[-1]
        if A[first] >= A[first+1]:
            ans+= A[first]
        else:
            ans+=(A[first+1])
        first = first + 2
    return ans

print(highscore(n))


# import sys
# input = sys.stdin.readline

# n  = int(input())
# score = [int(input().rstrip()) for _ in range(n)]
# score = [0] + score
# def highscore(n):
#     if n == 0:
#         return 0
#     ans = [score[1],score[-1]]
#     first = 2
#     for i in range(2, n-1):
#         if score[first] >= score[first+1]:
#             ans.append(score[first])
#         else:
#             ans.append(score[first+1])
#         first = first + 2
#     return sum(ans)

# print(highscore(n))