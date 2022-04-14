import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ans = str(A * B * C)

nums = '0123456789'

for num in nums :
    print(ans.count(num))