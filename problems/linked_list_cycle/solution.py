# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        curr2 = head
        
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next

            if curr1 == curr2:
                return True
            
        return False