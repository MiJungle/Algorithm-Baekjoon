

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
from collections import defaultdict
def solution(id_list, report, k):
    report = set(report)

    arr = defaultdict(list)
    count =defaultdict(int)
    for i in report:
        a, b= i.split()
        arr[a].append(b)
        count[b]+= 1
    need = []
    for i in count:
        if count[i] >= k:
            need.append(i)
    
    dd = defaultdict(int)

    for i in id_list:
        dd[i]

    for i in arr:
        for j in need:
            if j in arr[i]:
                dd[i] += 1 
    fin = []
    for i in dd:
        fin.append(dd[i])
    return(fin)    
print(solution(id_list, report, k))