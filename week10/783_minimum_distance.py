root = [4,2,6,1,3]

import sys

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    prev = -sys.maxsize #-9223372036854775807 (64-bit: the value will be 2^63 – 1)
    result = sys.maxsize # 9223372036854775807
    def minDiffInBST(self, root):
        if root.left:#왼쪽 노드가 있는 경우
            self.minDiffInBST(root.left) 
        self.result = min(self.result, root.val - self.prev)
        print(self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)   
        return self.result

print(Solution().minDiffInBST(root))