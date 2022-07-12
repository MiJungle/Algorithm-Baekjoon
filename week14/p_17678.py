timetable= 	["09:10", "09:09", "08:00"]	
n =2
t = 10
m = 2

def solution(n, t, m, timetable):
    timetable.sort()
    first = "09:00"
    bustime= [first]
    minute = first[3:5]
    hour= first[0:2]

    for i in range(n-1):
        minute = str(t+ int(first[3:5])).zfill(2)
        if int(minute) >=60 :
            hour = str(int(hour) + int(minute)//60).zfill(2)
            minute = str(int(minute) %60).zfill(2)
        bustimes = hour +":"+ minute
        bustime.append(bustimes)
    count = 0
    time = 0
    if len(timetable) < m*m:
        time = bustime[-1]
    if len(timetable) >= m*m and ( ( int(timetable[-1][0:2]) < int(bustime[-1][0:2]) ) or ( int(timetable[-1][0:2]) == int(bustime[-1][0:2]) and int(timetable[-1][3:5]) <= int(bustime[-1][3:5]) ) ):
        min = int(timetable[m-1][3:5]) - 1
        hr = timetable[m-1][0:2]
        if int(min) < 0:
            min = 60+int(min)
            hr = str(int(timetable[m-1][0:2]) - 1).zfill(2)
        time = hr + ":" + str(min).zfill(2)
    return time

    # return answer

print(solution(n,t,m,timetable))