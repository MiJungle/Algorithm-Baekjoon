import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

left = 1
right = max(arr)
def tree():
    global left, right
    if len(arr) == 1 and arr[0] == 0:
        return 0
    while left < right:
        ans =0
        mid = (left + right)//2
        for i in range(n):
            if arr[i] > mid:
                ans += arr[i] - mid
        if ans == m:
            return mid
        elif ans > m:
            left = mid + 1
        elif ans < m:
            right = mid -1
    return left

print(tree())