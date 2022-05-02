import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

A.sort()

left = 0
right = n-1
ans = []
big = 2e9 + 1

while left < right:
    k = A[left] + A[right]
    if abs(k)<big:
        big = abs(k)
        ans = [A[left], A[right]]
    if k < 0 :
        left += 1
    else:
        right -= 1
print(*ans, sep=' ')