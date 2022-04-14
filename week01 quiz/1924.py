import sys
input = sys.stdin.readline

x, y = list(map(int, input().split()))
enddate =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
day =['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN' ]

def whatday(x, y):
    global enddate, day
    date = y + sum(enddate[:x-1])
    if date % 7 == 1:
        print(day[0])
    elif date % 7 == 2:
        print(day[1])
    elif date % 7 ==3:
        print(day[2])
    elif date % 7 == 4:
        print(day[3])
    elif date % 7 == 5:
        print(day[4])
    elif date % 7 == 6:
        print(day[5])
    elif date % 7 == 0:
        print(day[6])

whatday(x,y)
