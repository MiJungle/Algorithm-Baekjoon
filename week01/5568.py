import sys
from itertools import permutations
input = sys.stdin.readline

n, k  = int(input()), int(input())
print(n,k)
cards = [input().rstrip() for _ in range(n)] ## 오른쪽 띄어쓰기 없애기
res = set() ## 빈 집합값
for per in permutations(cards, k): ## 순서있음 k 개수만큼 뽑은 세트 값을 
    res.add('-'.join(per)) # ##  per을 join 합쳐서 res 집합에 add해라 
print(res)
print(len(res))


##The rstrip() method removes any trailing characters 
# (characters at the end a string), space is the default trailing character to remove.

