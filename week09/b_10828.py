import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    m = list(map(str, input().split()))
    if m[0] == "push":
        ans.append(m[-1])
    elif m[0] =="pop":
        if len(ans)==0:
            print(-1)
        else:
            print(ans.pop())
    elif m[0] =="size":
        print(len(ans))
    elif m[0] =="empty":
        if len(ans)==0:
            print(1)
        else:
            print(0)
    elif m[0] =="top":
        if len(ans)==0:
            print(-1)
        else:
            print(ans[-1])


