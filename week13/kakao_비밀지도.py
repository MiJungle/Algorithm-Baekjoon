from collections import defaultdict


from collections import defaultdict
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

n = 6

def solution(n, arr1, arr2):
    ar1 = []
    ar2 = []
    for i in range(n):
        k= format(arr1[i], 'b')
        ar1.append(k)
        m = format(arr2[i], 'b')
        ar2.append(m)
    ans = []
    
    for i in range(len(ar2)):
        ans.append(str(int(ar1[i])+int(ar2[i])))

    dd = []
    for i in ans:
        i = list(map(str, i))
        dd.append(i)
    
    for i in dd:
        if len(i) != n:
            while len(i) != n:
                i.insert(0,'0')
    mk = []
    for i in dd:
        m =''.join(i)
        mk.append(m)
    m = [i.replace("1","#") for i in mk]
    s = [i.replace("2","#") for i in m]

    fin = [i.replace("0"," ") for i in s]

    return fin
    
print(solution(n,arr1,arr2))

