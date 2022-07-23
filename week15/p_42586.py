# import math
# progresses =	[99, 30, 55]
# speeds = [100, 30, 5]


# def solution(progresses, speeds):
    
#     days = []
#     for i in range(len(progresses)):
#         days.append(math.ceil((100-progresses[i])/speeds[i]))
#     answer = []
#     while days:
#         baepo = days.pop(0)
#         count = 1
#         while days and days[0] <= baepo:
#             baepo = days.pop(0)
#             count += 1
#         answer.append(count)
#     return answer

# print(solution(progresses,speeds))

import math
def solution(progresses, speeds):
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))

    answer = []
    index = 0
    for i in range(len(progresses)):
        if days[index] < days[i]:
            answer.append(i-index)
            index = i
    answer.append(len(progresses) - index)


    return answer