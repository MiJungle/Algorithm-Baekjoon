
def add_star(ptn):
    return"* " + ptn + " *"

def recur(n):
    if n == 1:
        return "*"
        
    else:
        return ["*"* (4*n-3) ]\
            +["*"+ ' '*(4*n-5) + "*"]\
        +list(map(add_star, recur(n-1)))\
        +["*" + ' '*(4*n-5) + "*"]\
        +["*"* (4*n-3)]    

print("\n".join(recur(int(input()))))