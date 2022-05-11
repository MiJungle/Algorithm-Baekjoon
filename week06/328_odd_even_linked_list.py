# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        odd = []
        even = []
        while node != None:
            if len(even)==0 or len(even)<= len(odd):
                even.append(node.val)
            else:
                odd.append(node.val)
            node = node.next    
        ans = even + odd
        cur = dummy = ListNode(0)
        for e in ans:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        