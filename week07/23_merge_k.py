import heapq
lists = [[1,4,5],[1,3,4],[2,6]]
#value 다 뽑아서 list에 담고 
#sorted 한다음에 한 리스트로 만들기
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        root = result = ListNode(None) 
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            result = result.next 
            if result.next:
                heapq.heappush(heap,(result.next.val, idx, result.next))
        return root.next