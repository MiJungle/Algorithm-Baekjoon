a = 12
b = 31


def solution(a, b):
    end = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["SUN","MON","TUE","WED","THU" "FRI","SAT"]    
    print(day[6])
    total = sum(end[:a-1]) + b
    if total %7 == 0:
        return day[4]
    elif total % 7 == 1:
        return day[5]
    elif total % 7 == 2:
        return day[6]
    elif total % 7 == 3:
        return day[0]
    elif total % 7 == 4:
        return day[1]  
    elif total % 7 == 5:
        return day[2]
    elif total % 7 == 6:
        return day[3]  

print(solution(a, b))