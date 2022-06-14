
#left 있으면 left 타고들어가고
#min value에는 min(현재 min 값, 뺀값)
#prev에 현재 노드값저장
# right 있으면 right 타고들어가고

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    prev = -2e9
    num = 2e9
    def minDiffInBST(self, root):
        if not root:
            return 
        if root.left:
            self.minDiffInBST(root.left)

        self.num = min(abs(self.num), abs(root.val - self.prev))
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right,)
        return self.num