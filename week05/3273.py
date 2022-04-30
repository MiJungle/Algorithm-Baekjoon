import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
x = int(input())

ans = 0
A.sort()
print(A)
left, right = 0, n-1
while left < right:
    if A[left] + A[right] == x:
        ans += 1
        left += 1
        right -= 1
    elif A[left] + A[right] <x:
        left += 1
    else:
        right -= 1

print(ans)
 


#시간초과 답변 1)
# n = int(input())
# A = list(map(int, input().split()))
# x = int(input())
# left, right = 0, 0 
# ans = 0
# for i in range(0,n):
#     for j in range(i+1,n):
#         if A[i] + A[j] == x:
#             ans += 1
# print(ans)

#시간초과 답변 2)
# n = int(input())
# A = list(map(int, input().split()))
# x = int(input())

# left, right = 0, 0 
# ans = 0

# while left != n:
#     for i in range(left+1, n):
#         if A[left] + A[i] == x:
#             ans += 1
#     left += 1

# print(ans)