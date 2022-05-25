n = int(input())
# 23승부터 나눠, 그래서 나눠지면 1, 안나눠지면 0 나눠떨어지면 0을 뒤에 i-1만큼 뱉고 출력 
# def recur(n,i):
#     if i == 0:
#         if n == 1:
#             print(1, end='')
#         else:
#             print(0, end='')
#         return
#     else:
#         k = n // 2**i
#         t = n - (2**i)*k
#         if t == 0:#나눠 떨어졌다
#             print(1, str(0)*(i-1), end='')
#             return
#         elif n> 2**i: # 2**i로 나눌 수 있을 때 
#             if k >=1:
#                 print(1, end='')
#             else: 
#                 print(0, end='')
#         elif n<=2**i:
#             print(0)

#         recur(t, i-1)
         
# recur(n,32)


def binary(n):
    if n > 1:
        binary(n // 2)
    return print(n % 2, end='')

binary(n)