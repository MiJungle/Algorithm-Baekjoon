
n = 2
t = 10
m = 2
timetable =["09:10", "09:09", "08:00"]

def solution(n, t, m, timetable):

    timetable.sort()
    print(timetable)
    
    first = "09:00"
    last = first
    if n*t >= 60: #버스 막차 시간 구하기
        last = str(int(first[0:2]) + ((n-1)*t//60)).zfill(2) + ":" + str(((n-1)*t)%60).zfill(2)
    else: 
        last = (first[0:2]) + ":"+ str(int(first[3:5]) + (n-1)*t).zfill(2)  
    print(last)
    ans = last
    if len(timetable) >= n* m:
        print(timetable[n*m-1])
        if int(timetable[n*m-1][0:2]) <= int(last[0:2]) and int(timetable[n*m-1][3:5]) <= int(last[3:5]):
            print("dd")
            if timetable[n*m-1][3:5] == "00":
                ans = str(int(timetable[n*m-1][0:2])-1).zfill(2) + ":" + "59"
            else:
                print(timetable[n*m-1])
                ans = timetable[n*m-1][0:2] + ":" + str(int(timetable[n*m-1][3:5])-1).zfill(2)
                print(ans)
    #         else:
    #             return last        
    # return ans

    #     ans = last
    # return ans

print(solution(n, t, m, timetable))

###시간대별로 - 인원을 생각해야함...