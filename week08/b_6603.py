# https://seolwonkoo.tistory.com/21
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(start, length):
    if length == 6:
        for i in range(6):
            print(answer[i], end = ' ')
        print()
    for i in range(start, a):
        answer[length] = arr[i]
        dfs(i+1, length+1)

while True:
    arr = list(map(int, input().split()))
    a = arr[0]
    arr = arr[1:]
    if a == 0:
        break
    answer = [0]*a
    dfs(0,0)
    print()



def DFS(L, BeginWith):
    if L == r:
        print(result)
    else:
        for i in range(BeginWith, len(n)):
            result[L] = [i]
            DFS(L+1, i+1)


n = [1,2,3]
r = 2

result = [0]* r

DFS(0, 0) #(0level, 0 beginwith)




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

# while True:
#     arr = list(map(int, input().split()))
#     k = arr[0]
#     r = 6
#     result = [0] *r
#     arr = arr[1:]
#     checklist = [0] *len(arr)
#     if k == 0:
#         break
#     DFS(0)
#     print()
    



# arr = [1,2,3]
# r = 2
# result = [0] *r
# checklist = [0] *len(n)
# DFS(0)






