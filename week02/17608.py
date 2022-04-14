import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())

M = [int(input().rstrip()) for _ in range(N)]
count = 1
d= M[-1] #주의: for 문 안에 넣어버리면 d가 갱신되더라도 다시 d = M[-1]이 되어버림
for i in range(len(M)-2, -1, -1 ):
    if M[i] > d:
        count+=1
        d = M[i]

print(count)


 