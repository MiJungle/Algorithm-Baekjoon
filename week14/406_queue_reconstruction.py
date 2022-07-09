import heapq
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

class Solution(object):
    def reconstructQueue(self, people):
        newpeople = sorted(people, key= lambda x: (x[0],-x[1]))
        ans = []
        while newpeople: 
            m = newpeople.pop(-1)
            ans.insert(m[1], m)

        print(ans)

Solution().reconstructQueue(people)