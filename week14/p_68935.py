import string
def solution(n):
    def convert(num, base) :
        tmp = string.digits+string.ascii_lowercase
        print(tmp)
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base)+ tmp[r]

    m = convert(n,3)
    k = str(m)[::-1]
    fin = int(k,3)
    return fin
print(solution(45))


# def solution(n):
#     answer = 0
#     rev_base = ''
#     while n > 0:
#         n, mod = divmod(n, 3)
#         rev_base += str(mod)
#     answer = int(str(rev_base), 3)
#     return answer