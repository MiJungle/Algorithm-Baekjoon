import sys
sys.stdin = open("input.txt")
input =sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting = sorted(meeting,key=lambda x: (x[1], x[0]))

ans = 1
k = meeting[0][1]
for i in range(1,len(meeting)):
    if meeting[i][0] >= k:
        ans += 1
        k = meeting[i][1]
print(ans)