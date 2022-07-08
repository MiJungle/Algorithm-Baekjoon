import string
def solution(n):
    def convert(num, base) :
        tmp = string.digits+string.ascii_lowercase
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base)+ tmp[r]

    m = convert(n,3)
    k = str(m)[::-1]
    fin = int(k,3)
    return fin