class Solution(object):
    def mergeKLists(self, lists):
        root = Listnode(None)
        heap = []
        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(heap, (lists[i].val i, lists[i]))
        while heap:

            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]
            result = result.next
            if result.next:
                heapq.heappush(heap,(result.next.val, idx, result.next))
        return root.next

