n = int(input())

def recur(n,i):
    if i == 0:
        return
    else:
        if n >= 2**i:
            k = n // 2**i
            t = n - (2**i)*k
            if k >=1:
                print(1, end=' ')
            else: print(0, end=' ')
        else:
            recur(t, i-1)
         
recur(n,10)