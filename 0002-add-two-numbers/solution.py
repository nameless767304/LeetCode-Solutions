# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        carry = 0

        curr_node = ListNode()
        head = curr_node

        while True:
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            num = num1 + num2 + carry

            if num >= 10:
                carry = 1
                num -= 10
            else:
                carry = 0

            curr_node.next = ListNode()
            curr_node = curr_node.next
            curr_node.val = num

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

            if l1 is None and l2 is None and carry == 0:
                break

        return head.next




        
