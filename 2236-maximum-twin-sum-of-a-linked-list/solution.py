# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        node = head
        max_val = 0

        while node is not None:
            vals.append(node.val)
            node = node.next

        for idx in range(len(vals) // 2):
            max_val = max(max_val, vals[idx] + vals[- idx - 1])
            
        return max_val
