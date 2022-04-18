# 소스: https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1197%EB%B2%88-%EC%B5%9C%EC%86%8C-%EC%8A%A4%ED%8C%A8%EB%8B%9D-%ED%8A%B8%EB%A6%AC

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


V, E = map(int, input().split())
parent = [i for i in range(V+1)] #정점의 개수 만큼 parents에 담음
vertices = [list(map(int, input().split())) for _ in range(E)] #간선의 개수만큼 담음
vertices.sort(key=lambda x: x[2]) #간선을 가중치 (C- index 2) 기준으로 나열
print(parent[1], vertices)

def find_parent(parent, x):  #두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소 (즉, 루트 노드)를 확인
    if parent[x] != x: #parents에 있으면 x그대로 리턴
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x]

def union_parent(parent, a, b): #두개의 집합을 합침
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: #둘중 숫자가 작은것으로 parent 를 만들어줌
        parent[b] = a
    else:
        parent[a] = b
# parent = [0, 1, 2, 3] vertices = [[1, 2, 1], [2, 3, 2], [1, 3, 3]] 
#[1,2,1]] 에서 find(parent, 1) 은 1,find(parent, 2) 은 2가 된다. 
# 1<2 이기 때문에 parent[2] =1 이 됨
# [2,3,2] 에서 find(parent, 2) 는 parent[2]!= 2이기 때문에 parent[2] = find_parent(parent, 1)인 1이 됨
# find_parent(parent, 2) 와 find_parent(parent,3 ) 은 값이 다르기 때문에 3을 2에 합쳐준다

result = 0
for vertice in vertices:
    a, b, cost = vertice
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)

