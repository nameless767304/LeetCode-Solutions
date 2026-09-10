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
        nums = [node.val]

        if node.left:
            nums.extend(self.exploreSubtree(node.left))
        if node.right:
            nums.extend(self.exploreSubtree(node.right))

        if node.val == int(sum(nums) / len(nums)):
            self.ans += 1

        return nums