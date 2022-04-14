import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N, B = map(int,input().split())
num = [list(map(int, input().split())) for _ in range(N)]

def prod(a, b):
    n = len(a) 
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    remainder(c)
    return c

def remainder(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            A[i][j] %= 1000

def dnq(A,B):
    if B ==1 : return A
    x = dnq(A, B//2)
    if B % 2: return prod(prod(x,x), A)
    else: return prod(x,x)

remainder(num)
print("\n".join(map(lambda x: " ".join(map(str, x)), dnq(num, B))))








# N, B = map(int,input().split())
# num = [list(map(int, input().split())) for _ in range(N)]

# column = []

# for j in range(N):
#     li = []
#     for i in num:
#         li.append(i[j])
#     column.append(li)

# n = []
# for i in range(N):
#     a = []
#     k = 0
#     for j in range(N):
#         k += num[i][j] * num[j][i]
#     print(k)

# print(a)

# def matrixpower(a, B):


#     if B == 1:
#         return  a % 1000
#     else:
#         ans = matrixpower(a, B//2)
#         if B % 2 == 0:
#             return ans * ans % 1000
#         else:
#             return ans * ans * a % 1000 % 1000


# print(matrixpower(a, B))
