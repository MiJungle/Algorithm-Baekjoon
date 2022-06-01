import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int, input().split()))
tree.sort()

left = 1
right = max(tree)
while left <= right:
    mid = (left+right)//2
    ans = 0
    for t in tree:
        if t > mid:
            ans += t-mid
    if ans >= m:
        left = mid+1
    else:
        right = mid-1

print(right)







 #최대 길이는 마지막 나무 높이만큼 
#     num = 0
#     idx = 0
#     while num != m and idx != len(trees)-1:
#         if trees[idx] > length:
#             num += trees[idx]- length
#             idx+= 1
#             print(idx)
#         return length
#     if num > m:
#         length = length + 1
#     else: 
#         length = length - 1

#     return length
# print(cut_tree())