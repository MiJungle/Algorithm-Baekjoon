import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

m = input().strip()
m = m.upper()

counts = dict()
for i in m:
    counts[i] = counts.get(i,0) +1

d = max(counts, key = counts.get)
count =0
for keys in counts:
    if counts[keys] == counts[d]:
        count += 1
if count != 1:
    print('?')
else:
    print(d)
