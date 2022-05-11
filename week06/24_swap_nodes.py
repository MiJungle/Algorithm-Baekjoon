#소스: https://joecho.tistory.com/entry/leetcode24

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        firstNode = head
        
        while head and head.next:
            currentNode = head
            nextNode= currentNode.next
            currentNode.val, nextNode.val = nextNode.val, currentNode.val
            head = nextNode.next
        
        return firstNode

# 리스트로만든다
# 짝수번쨰 요소와 홀수번쨰 요소를 추출한다
# 홀수리스트 끝 숫자부터
# 짝수리스트 끝 숫자랑 연결해준다
# 그럼 그 짝수 수랑 홀수수랑 또 연결해준다
# 0번째 수가 될때까지 