from collections import deque
people = [30,30,30]		
limit = 100

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while people:
        left = people.popleft()
        
        if not people:
            return answer + 1

        else:
            right = people.pop()
            if right + left > limit: #작은 경우 생각 안해도 되는게, limit 보다 클때만 보트를 하나씩 더해주면됨. 
                people.appendleft(left)
        answer += 1 #어차피 1명밖에 못탐. 
    return answer