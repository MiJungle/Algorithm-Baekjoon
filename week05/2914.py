import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

m = input()
cro =['c=', 'c-','dz=','d-','lj','nj','s=','z=']
ans = 0
for i in range(len(m)):
    if i <=len(m)-2 and m[i] == 'c' and (m[i+1] =='=' or m[i+1] =='-'):
        ans += 1
    elif i <=len(m)-3 and m[i] == 'd' and ((m[i+1]== 'z' and m[i+2] == '=') or m[i+1]=='-') :
        ans +=1
    elif i >= 1 and m[i] =='j' and (m[i-1] =='l' or m[i-1] == 'n'):
        ans += 1
    elif i >=1 and m[i] == '=' and (m[i-1] =='s' or m[i-1] == 'z'):
        ans +=1

print(ans)