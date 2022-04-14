import sys
from itertools import combinations
input = sys.stdin.readline

m = 1
S= []
while m!= 0:
    m = list(map(int, input().split()))
    S.append(m)
    if m == [0]:
        break

for i in range(len(S)-1):
    for com in combinations(S[i][1:],6):
        print(*com, sep= ' ')
    print()
