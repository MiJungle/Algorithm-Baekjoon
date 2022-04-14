import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

x = [w,0]
y = [h,0]
for i in range(n):
    a, b = map(int, input().split())
    if a==0:
        y.append(b)
    else:
        x.append(b)

x.sort()
y.sort()

width = []
for i in range(1,len(x)):
    a = x[i]- x[i-1]
    width.append(a)

height = [0]
for i in range(1,len(y)):
    b = y[i]- y[i-1]
    height.append(b)

ans = max(width) * max(height)
print(ans)

