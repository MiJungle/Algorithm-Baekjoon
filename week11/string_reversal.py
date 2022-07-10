from collections import deque
lst = "the simple engineer"
lst = deque(lst)

def recur(n):
    if n == 0:
        return 
    else:
        k = lst.pop()
        lst = k+ recur(n-1)
        print(lst, end='')

recur(len(lst))
    