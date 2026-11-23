# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head

        while curr is not None:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head