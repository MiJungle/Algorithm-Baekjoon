import sys
sys.stdin = open("input.txt")

N = int(input())

M = [input().rstrip() for _ in range(N)]

ans = []
for i in M:
    if i[:2] == "pu":
        ans.append(i[5:])
    elif i == "pop":
        if len(ans) == 0:
            print(-1)
        else:
            print(ans.pop(-1))
    elif i == "top":
        if len(ans)== 0:
            print(-1)
        else:
            print(ans[-1])
    elif i =="size":
        print(len(ans))
    elif i =="empty":
        if len(ans) == 0:
            print(1)
        else:
            print(0)


