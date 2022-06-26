import collections

from sympy import N
tasks = ["A","B","C","D","E","A","B","C","D","E"]
n = 4

li = collections.Counter(tasks)
count = 0
print(li)
# if n == 0:
#     print(len(tasks))

# for key, value in li.items():
#     if value > 1:
#         count += (value-1) * n
#     else:
#         count += value
# print(count)