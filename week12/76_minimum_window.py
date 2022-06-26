# 소스: https://www.google.com/search?q=leetcode+76+python&newwindow=1&sxsrf=ALiCzsZCuTladymxelHoE7LfksgbvXWjjQ%3A1656218811855&ei=u-S3YrTsM8iFoAT0grmgDQ&ved=0ahUKEwj0tc3vp8r4AhXIAogKHXRBDtQQ4dUDCA4&uact=5&oq=leetcode+76+python&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEOgYIABAeEAdKBAhBGABKBAhGGABQAFiOFGDwFWgAcAF4AIAB1wGIAZEJkgEFMC44LjGYAQCgAQHAAQE&sclient=gws-wiz

import collections
s = "ADOBECODEBANC"
t = "ABC"
need = collections.Counter(t) #데이터 개수 셀 때
# print(need) Counter({'A': 1, 'B': 1, 'C': 1})
# print(collections.Counter(s)) Counter({'A': 2, 'D': 2, 'O': 2, 'B': 2, 'E': 2, 'C': 2, 'N': 1})
missing = len(t)
left = start = end = 0

# 오른쪽 포인터 이동
for right, char in enumerate(s, 1):
    # missing -= need[char] >0 # missing 은 need[char] 뺀값이 0보다 크냐? bool 값을 가지고 있음
    missing -= need[char] >0 #필요한 단어들이 아직 남아있음 
    need[char] -= 1 #반복문 돌때마다 s에 필요한 char있으면 뺌

    # 필요 문자가 0이면 왼쪽 포인터 이동 판단(최소 범위로 쫍히기 위함)
    if missing == 0: 
        while left < right and need[s[left]] < 0: #s[left] 에 있는 문자의 need 개수가 음수일때,
            need[s[left]] += 1
            left += 1

        if not end or right - left <= end - start: #end == 0 이거나 right - left <= end - start 일때
            start, end = left, right #start 는 left 값을, end 는 현재 반복문에서 돌고 있는 index 수를 가짐

        need[s[left]] += 1
        missing += 1
        left += 1

print( s[start:end])










# from collections import defaultdict
# class Solution(object):
#     def minWindow(self, s, t):
#         need = collections.Counter(t)
#         missing = len(t)
#         left = start = end = 0

#         # 오른쪽 포인터 이동
#         for right, char in enumerate(s, 1):
#             missing -= need[char] > 0
#             need[char] -= 1

#             # 필요 문자가 0이면 왼쪽 포인터 이동 판단th
#             if missing == 0:
#                 while left < right and need[s[left]] < 0:
#                     need[s[left]] += 1
#                     left += 1

#                 if not end or right - left <= end - start:
#                     start, end = left, right

#                 need[s[left]] += 1
#                 missing += 1
#                 left += 1

#         return s[start:end]