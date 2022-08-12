
graph = [[0]*1000 for _ in range(1000)]

while True:
    try:
        dir, p1, t, p2 = list(map(str, input().split()))
        p1 = list(map(int, p1.split(',')))
        p2 =  list(map(int, p2.split(',')))

        if dir == "front":
            for dx in range(p2[0]-p1[0]+1):
                for dy in range(p2[1]-p1[1]+1):
                    graph[p1[0]+dx][p1[1]+dy] = 1
        
        elif dir =="back":
            for dx in range(p2[0]-p1[0]+1):
                for dy in range(p2[1]-p1[1]+1):
                    graph[p1[0]+dx][p1[1]+dy] = 2


        elif dir =="flip":
            for dx in range(p2[0]-p1[0]+1):
                for dy in range(p2[1]-p1[1]+1):
                    if graph[p1[0]+dx][p1[1]+dy] == 1:
                        graph[p1[0]+dx][p1[1]+dy] = 2
                    elif graph[p1[0]+dx][p1[1]+dy] == 2:
                        graph[p1[0]+dx][p1[1]+dy] = 1
                    elif graph[p1[0]+dx][p1[1]+dy] == 0:
                        graph[p1[0]+dx][p1[1]+dy] = 1

        answer = 0
        for i in graph:
            answer+= i.count(1)

    except:
        break
print(answer)
    



