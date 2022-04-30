import sys
input = sys.stdin.readline

li = input().split('-')
ans = []
for i in li:
    s = i.split('+')
    num =0
    for j in s:
        num += int(j)
    ans.append(num)

n = ans[0]
for i in range(1,len(ans)):
    n-= ans[i]
print(n)