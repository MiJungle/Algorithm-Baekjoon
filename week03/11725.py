# 소스:https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0]*(n+1)

for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(start, tree, parents):
    for i in tree[start]: ## tree[1]=[6,4] 에서 6의 parents가 없는경우 1을 6의 parents로 설정한다. 
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, tree, parents)
for i in range(2, n+1):
    print(parents[i])