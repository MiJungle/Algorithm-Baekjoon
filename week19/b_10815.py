import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))
k = int(input())
card = list(map(int, input().split()))

ans = []

for i in card:
    if i in arr:
        ans.append(1)
    else:
        ans.append(0)
print(*ans,end=" ")

# for i in card:
#     if i in arr:
#         ans.append(1)
#     else:
#         ans.append(0)
# print(ans)
# for i in range(k):
#     left =0 
#     right = n-1
#     while left < right:
#         mid = (left+right)//2
#         if card[i] == arr[mid]:
#             ans.append(1)
#             break
#         else:
#             if card[i]< arr[mid]:
#                 right = mid-1
#             elif card[i]>arr[mid]:
#                 left = mid+1
#         print(mid)
#     if len(ans)!= i+1:
#         ans.append(0)       
        
# print(ans)