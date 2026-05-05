# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or head is None:
            return head

        curr_check = head
        length = 0
        while True:
            length += 1
            if curr_check.next is None:
                curr_check.next = head
                break
            else:
                curr_check = curr_check.next

        k = length - (k % length)
        curr = head
        new_head = None

        while True:
            if k == 1:
                new_head = curr.next
                curr.next = None
                break
            curr = curr.next
            k -= 1
            
        return new_head



