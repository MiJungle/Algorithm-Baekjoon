import sys, math

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

ans =[]
for num in nums:
    if num ==1:
        ans.append(1)
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            ans.append(num)


nums2 = list(set(nums))
result1 = list(set(ans))
result2 = len(nums2) - len(result1)
print(result2)


