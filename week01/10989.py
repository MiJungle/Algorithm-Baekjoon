from operator import indexOf
import sys

input =  sys.stdin.readline

n = int(input())
ans = [0] * 10001

for i in range(n):
    data = int(input())
    ans[data] += 1

for i in range(10001):
    if ans[i] != 0:
        for j in range(ans[i]):
            print(i)
