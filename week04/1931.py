import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

#접근방법: 첫번째꺼 넣고 그 [1] 값보다 큰 값을 넣고 count +1 

N = int(input())
time = [[0]*2 for _ in range(N)]
for i in range(N):
    s,e =  map(int, input().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x:(x[1],x[0])) #이른 시간대에 끝나는 거 위주로

cnt = 1
end_time = time[0][1]
for i in range(1,N):
    if time[i][0] >= end_time: #시작시간이 end_time 보다 늦거나 같으면
        cnt+= 1
        end_time = time[i][1]   # end_time 리셋
print(cnt)

    