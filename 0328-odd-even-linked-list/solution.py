# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head       

        if head is None: return None

        odd_node = dummy.next
        even_node = dummy.next.next
        even_first_node = even_node

        while even_node and even_node.next:
            odd_node.next = even_node.next
            odd_node = odd_node.next
            even_node.next = odd_node.next
            even_node = even_node.next

        odd_node.next = even_first_node

        return dummy.next 
