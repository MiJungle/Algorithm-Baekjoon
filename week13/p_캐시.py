cacheSize = 0
cities = 	["Jeju", "Pangyo","Jeju", "Pangyo","Jeju"]

def solution(cacheSize, cities):
    if cacheSize ==0:
        return len(cities) *5
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    li = []
    ans = 0
    for i in cities:
        if i in li:
            ans += 1
            li.remove(i)
            li.append(i)
        else:
            ans += 5
            if len(li) >= cacheSize: 
                li.pop(0)
                li.append(i)
            else:
                li.append(i)           
            
    return ans

###처음에 cache size 만큼 배열을 잘랐느데 생각해보니까 그러면 애초에 중복된걸 리스트에 담아버리게 됨. 
##arr = [:cachesize] 이렇게 하면 ["jeju","jeju"] 이런경우가 생겨버림