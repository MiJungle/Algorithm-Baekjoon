from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))

ans = []
for com in combinations(num, 3):
    if sum(com) <= M:
        ans. append(sum(com))

print(max(ans))


    