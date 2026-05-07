#week11-2.py binary tree 最後一題
#leetcode 236. Lowest Common Ancestor of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a = []
        def helper(root):
            count = 0 #請問你下面累積幾個p或q的node
            if root==None: return 0 #沒有東西
            if root==p or root==q:count +=1
            count +=helper(root.left)
            count +=helper(root.right)
            if count == 2:#蒐集其兩個
                a.append(root)
            return count #現在收集幾個呢
        helper(ro
