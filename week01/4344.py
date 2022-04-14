
####다시 풀어보기 

import sys
input = sys.stdin.readline

n = int(input())
y = [list(map(int, input().split())) for _ in range(n)]

m = []
for li in y:
    M = sum(li) - li[0]
    aver = M/li[0]
    li.append(aver)
    m.append(li)

ans = []
for li in y: 
    count = 0
    for i in range(1, len(li)-1):
        s = []
        if li[i] > li[-1]:
            count += 1
    print(format(count/li[0]*100,'.3f')+"%")
