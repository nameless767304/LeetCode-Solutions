# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.exploreSubtree(root)
        return self.ans

    def exploreSubtree(self, node) -> list:
        nums = node.val
        count = 1

        if node.left:
            nums_subtree, count_subtree = self.exploreSubtree(node.left)
            nums, count = nums + nums_subtree, count + count_subtree 
        if node.right:
            nums_subtree, count_subtree = self.exploreSubtree(node.right)
            nums, count = nums + nums_subtree, count + count_subtree
        if node.val == int(nums / count):
            self.ans += 1

        return nums, count