#visited 숫자랑 numcourses 숫자가 같으면 true, 아니면 false

import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        traced = set()
        
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            return True
    
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True



# import collections
# numCourses = 2
# prerequisites = [[1,0],[0,1]]

# graph = collections.defaultdict(list)
# for i in prerequisites: 
#     graph[i[0]].append(i[1])

# visited = []

# def dfs(prerequisites[0]):
#     visited.append(prerequisites[0])
#     for a in graph[prerequisites[0]]:
#         if not a in visited:
#             visited= dfs(a)
#     return visited
# print(dfs(prerequisites[0]))
        
