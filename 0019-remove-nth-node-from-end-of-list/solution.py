# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        li_front = dummy
        li_back = dummy

        for _ in range(n):
            li_front = li_front.next

        while li_front.next:
            li_front = li_front.next
            li_back = li_back.next
                  
        li_back.next = li_back.next.next

        return dummy.next
