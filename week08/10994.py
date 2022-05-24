n = int(input())

def recur(n):
    if n == 1:
        print("*")
    else:
        print("*"* (4*n-3))
        print("*" + ' '*(4*n-5) + "*")
        print('*', end=' ')
        recur(n-1)
        print("*")  
        print("*" + ' '*(4*n-5) + "*")  
        print("*"* (4*n-3))      

recur(n)