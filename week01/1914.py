n = int(input())

def Hanoi(n,start,end):
    if n == 0: 
        return
    spare = 6 - start - end    
    Hanoi(n-1, start, spare)
    Move(n, start, end) 
    Hanoi(n-1, spare, end) 


def Move(n, orig, dest):
    print(orig, dest) 

if n <= 20:
    count = 2 ** n - 1
    print(count) 
    Hanoi(n, 1, 3)
elif n > 20:
    count = 2 ** n - 1
    print(count)
