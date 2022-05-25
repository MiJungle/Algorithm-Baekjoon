n = int(input())

def recur(n):
    if n == 1:
        print("*", end=' ')
        
    else:
        print("*"* (4*n-3))
        print("*" + ' '*(4*n-5) + "*")
        print("*", recur(n-1), "*")
        print("*" + ' '*(4*n-5) + "*")  
        print("*"* (4*n-3))      

recur(n)