import heapq
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

heap = []
for person in people: 
    heapq.heappush(heap, (-person[0], person[1])) #키큰 순서대로 정렬
#heap = [(-7, 0), (-6, 1), (-7, 1), (-4, 4), (-5, 0), (-5, 2)]
result = []
while heap:
    person = heapq.heappop(heap) #가장 작은 원소를 뱉어냄(가장 키큰 사람)
    result.insert(person[1],[-person[0], person[1]]) #그 다음 오는 애가 키큰애 밀어냄- 키큰애 앞에 작은애가 몇명있는지는 안중요함,
    #일단 키큰애들 위주로 person[1] 기준으로 넣고(큰애들끼리 누가 앞에 있어야하는지를 정함) 작은애들이 마지막에 넣어지면서 확실히 정렬이 되게끔. 
#result = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
print(result)