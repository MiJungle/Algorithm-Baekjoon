import sys
input = sys.stdin.readline

N = list(map(str, input().strip()))

ans=[]
newli = N
print(newli)
while len(newli) <=3:
    for i in range(len(newli)%4 +1):
        if newli[i: i+ 4] == ['P', 'P', 'A', 'P'] : #PPAP가 연속으로 나오면
            ans.append("P") #새로운 리스트에 P를 더해준후 
            li = N[i+4: len(N)] 
            newli = ans + li #P와 PPAP 연속으로 나온 것의 뒤편을 다시 합쳐준다. ?? 그러면 앞에 숫자들은??
            print(newli)

        if len(newli) <= 3 and newli !=['P', 'P', 'A', 'P']:
            print("NP")
        elif newli ==['P', 'P', 'A', 'P']:
            print("PPAP")


    
        
