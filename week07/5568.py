import sys
from itertools import permutations
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
k = int(input())
m = [input().strip() for _ in range(n)]

ans  = permutations(m,k )
fin = []
for i in ans:
    k = ''.join(i)
    fin.append(k)
fin = list(set(fin))

print(len(fin))

#k = 2, 3, 4 이다 
# 중복되는 숫자가 있고, 그 크기가 k랑 작거나 같은 경우
# 중복되는 숫자가 있고, 그 크기가 k 보다 큰 경우
# 아 일단 다 싸그리 숫자를 만들고, set 함수를 써서 중복되는 숫자 제거 
