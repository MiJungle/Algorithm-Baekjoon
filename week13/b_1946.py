import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for i in range(int(input())):
    t = int(input())
    spec = [list(map(int,input().split())) for _ in range(t)]
    spec = sorted(spec, key = lambda x: (x[0],x[1]))
    start = spec[0][1]
    count = 1
    for i in range(len(spec)):
        if spec[i][1] < start:
            count += 1
            start = spec[i][1]
    print(count)