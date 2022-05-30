import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline 

n = int(input())
k = int(input())
arr = [int(input().rstrip()) for _ in range(n)]
result = [0] *k
checklist = [0] *len(arr)
ans = []

def DFS(L):
    global ans
    if L == k:
        print(result)
    else: 
        for i in range(len(arr)):
            if checklist[i] == 0:
                result[L] = arr[i]
                checklist[i] = 1
                DFS(L+1)
                checklist[i] = 0
                
DFS(0)
print(ans)


















# def DFS(L):
#     if L == r:
#         print(result)
#     else: 
#         for i in range(len(arr)):
#             if checklist[i] == 0:
#                 result[L] = arr[i]
#                 checklist[i] = 1
#                 DFS(L+1)
#                 checklist[i] = 0

# n = [1,2,3]
# r = 2
# result = [0] *r
# checklist = [0] *len(n)
# DFS(0)
