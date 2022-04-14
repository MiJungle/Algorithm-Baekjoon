import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
M = [input().rstrip() for _ in range(N)]
ans = deque() ##list로 선언해서 pop(0)을 하게 되면 첫번째 element를 pop하고나서 나머지
#element들의 인덱스를 1칸씩 당기는 과정에서 O(n)의 계산량이 발생한다.
#따라서 deque를 이용한다음 popleft를 써준다
for i in M: 
    if i[:2] == "pu":
        ans.append(i[5:])
    elif len(ans) == 0 and (i == "pop" or i == "front" or i == "back"):
        print(-1)
    elif i == "pop":
        print(ans[0])
        ans.popleft()
    elif i == "size":
        print(len(ans))
    elif i == "empty":
        if len(ans) == 0:
            print(1)
        else:
            print(0)
    elif i == "front":
        print(ans[0])
    elif i == "back":
        print(ans[-1])
