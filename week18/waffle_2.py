import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def main():
    user = list(map(int, input().split()))
    user1 = list(map(int,input().split()))
    user2 = list(map(int,input().split()))
    user3 = list(map(int,input().split()))


    x= dict()
    y= dict()
    z= dict()
    for i in range(1,len(user1)):
        if i %2 !=0:
            x[str(user1[i-1])]= x.get(str(user1[i-1]),0) + user1[i]

    for i in range(1,len(user2)):
        if i %2 !=0:
            y[str(user2[i-1])]= y.get(str(user2[i-1]),0) + user2[i]

    for i in range(1,len(user3)):
        if i %2 !=0:
            z[str(user3[i-1])]= z.get(str(user3[i-1]),0) + user3[i]
    answer = []
    for key,values in x.items():
        if values >= 20 and key in y and key in z:
            if y[key]>=20 and z[key]>=20:
                answer.append(str(key))
    ans = ' '.join(answer)
    return len(answer),ans

a, b = main()
print(a,b, end=' ')
