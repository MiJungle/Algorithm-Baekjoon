import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

K = int(input())

ans = []
for i in range(K):
    m = int(input())
    if m == 0:
        ans.pop(-1)
    else:
        ans.append(m)
print(sum(ans))
