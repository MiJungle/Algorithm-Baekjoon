
# def solution(lines):
#     answer = 0
#     log = [] # log의 (시작시간, 끝시간) 저장

#     for line in lines:
#         date, s, t = line.split() # 날짜, 응답완료시간, 처리시간
#         s = s.split(':')
#         t = t.replace('s', '')  
    
#         end = (int(s[0])*3600 + int(s[1])*60 + float(s[2])) * 1000 # 끝시간을 msec 단위로 저장
#         start = end - float(t)*1000 + 1 # 시작 시간을 msec 단위로 저장
#         log.append([start, end])

#     for x in log:
#     	# 최대 초당 처리량 구하기
#         answer = max(answer, throughput(log, x[0], x[0] + 1000), throughput(log, x[1], x[1] + 1000))

#     return answer

# # 초당 처리량을 구하는 함수
# def throughput(log, start, end):
#     cnt = 0
#     for x in log:
#         if x[0] < end and x[1] >= start:
#             cnt += 1
#     return cnt
def solution(lines):
    arr = []
    answer = 0
    for line in lines:
        date, time, t = line.split()
        h,m,s = time.split(":")
        t= t.replace("s",'')
        end = (int(h)*3600 + int(m)*60 + float(s))*1000
        start = end - float(t)*1000 + 1 
        arr.append([start,end])

    for i in arr:  
        answer = max(answer, throughput(arr,i[0], i[0]+1000), throughput(arr, i[1], i[1]+1000))
    return answer
        
def throughput(arr,start, end):
    count = 0
    for i in arr:
        if i[0] < end and i[1] >= start:
            count += 1
    return count


lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))
# 출처: https://mjmjmj98.tistory.com/127 [Live passionate😎:티스토리]