# 소스: https://haesoo9410.tistory.com/252

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
    while stack:
        if tower[stack[-1]] >= tower[i]:  # index 뒷번호 위주로 크면 바로 그게 답이 되게끔.
            answer.append(stack[-1] + 1)
            break
        else:
            stack.pop()             #아닌 경우 stack에서 계속 숫자를 뺌
    if not stack:
        answer.append(0)
    stack.append(i)
print(' '.join(list(map(str, answer))))