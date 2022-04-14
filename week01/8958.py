
import sys
input = sys.stdin.readline

N = int(input())
d = []
for i in range(N):
    m = list(map(str, input()))
    d.append(m)

ans = []
for i in range(N):
    m = []
    count = 0
    for j in range(len(d[i])):
        if d[i][j] == 'O':
            count= 1+ count
            m.append(count)
        else:
            count = 0
    ans.append(m)

for ans in ans:
    print(sum(ans))