from itertools import combinations
import sys

input = sys.stdin.readline
m = [int(input().rstrip()) for _ in range(9)]

for num in combinations(m, 7):
    if sum(num) == 100 and len(num) == 7:
        ans =list(num)
        ans.sort()

for n in ans:
    print(n)

