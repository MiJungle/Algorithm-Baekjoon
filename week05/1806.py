import sys
sys.stdin = open('input.txt')
input =sys.stdin.readline

n,s = map(int, input().split())
k = list(map(int, input().split()))

ans = 0
num = []
left = 0
for i in range(n):
    left = i
    right = left+ 1
    num.append(k[left])
    num = []
    print(right)
    while right != n-1: 
        num.append(k[right])
        if sum(num) < 15:
            right += 1
        else: 
            ans = len(num)
            continue
print(ans)