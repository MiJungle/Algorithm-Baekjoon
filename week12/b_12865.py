import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, k = map(int,input().split())
thing = [[0,0]]
for _ in range(n):
    thing.append(list(map(int,input().split())))

bag = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1): 
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]
        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-w]+ v)
print(bag)
print(bag[n][k])




#헹: 무게
#열: 물건들의 무게와 가치 
# max([i-1], [i-1][j-k]])