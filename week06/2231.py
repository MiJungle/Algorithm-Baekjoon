import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
fin = []
finn= []
for m in range(n//2, n):
    k = str(m)
    ans = int(k)
    for i in k:
        ans += int(i)
    if ans == n:
        finn.append(ans)
    else:
        print(0)
while finn:
    print(min(finn))


