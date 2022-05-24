n = int(input())
print(n)
def recur(n):
    if n ==1:
        return
    else:
        if n % 2 == 0:
            k = n//2 
        else:
            k = 3*n + 1
        print(k)
        recur(k)
recur(n)