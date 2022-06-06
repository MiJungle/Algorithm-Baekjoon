import sys
import time
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
ans = [0]* n
while arr:
    start = time.time() 
    num = arr.pop()
    for i in range(len(arr)-1, 0, -1):
        if arr[i]>=num:
            ans[len(arr)]= i+1
            break
print(ans)
print("time :", time.time() - start)












#시간초과
# n = int(input())
# arr = list(map(int, input().split()))
# ans = [0]* n
# while arr:
#     num = arr.pop()
#     for i in reversed(arr):
#         if i>=num:
#             ans[len(arr)]= arr.index(i)+1
#             break

# print(ans)