a,b,c = map(int,input().split())

x= dict()
y = dict()
z= dict()
for i in range(a):
    id,num = map(int,input().split())
    x[id] = x.get([id], 0) + 1
print(x)