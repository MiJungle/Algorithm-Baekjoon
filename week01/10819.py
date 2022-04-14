import sys , random, math
from itertools import permutations

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

per = permutations(m)
ans =0

for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]- i[j+1])
    if s > ans:
        ans = s

print(ans)