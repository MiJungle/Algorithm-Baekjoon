from collections import defaultdict
id_list=["con", "ryan"]
report=	["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

report =sorted(set(report), key=report.index)

m = defaultdict(int)
n = defaultdict(list)
for i in report:
    a,b = i.split()
    m[b] += 1
    n[a].append(b)

for i in id_list:
    if i not in n:
        n[i]

li = []
for i in m:
    if m[i] >= k:
        li.append(i)

ans = []

for i in n:
    count =0
    for j in li:
        if j in n[i]:
            count += 1
    ans.append(count)
print("[{}]".format(",".join(map(repr, ans))))

