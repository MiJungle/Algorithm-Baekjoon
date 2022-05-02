import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n,s = map(int, input().split())
k = list(map(int, input().split()))

k.sort()
left = 0
right = n-1
big = 2e9 + 1
ans =[]
m = 0
while left < right:
    m += k[left] 
    if m == s:
        ans = [m]

    if m <s:
        left += 1
    else:
        right -= 1
        
