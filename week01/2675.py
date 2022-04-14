import sys
input = sys.stdin.readline

N = int(input())
b = []
for i in range(N):
    a = list(input().split())
    b.append(a)

l = []
for i in range(N):
    m =[]
    for j in range(len(b[i][1])):
        m.append(int(b[i][0])* b[i][1][j])
    l.append(m)

for i in range(N):
    m = ''.join(l[i])
    print(m)
