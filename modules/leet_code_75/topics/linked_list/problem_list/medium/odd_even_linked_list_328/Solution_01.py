"""
    328. Odd Even Linked List
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            curr_node = head
            even_node = head.next
            count = 0
            while curr_node.next.next is not None:
                past_next_node = curr_node.next
                curr_node.next = curr_node.next.next
                curr_node = past_next_node
                count += 1
            if count != 0 and count%2 == 0:
                curr_node.next.next = None
                curr_node.next = even_node
            elif count != 0 and count%2 != 0:
                curr_node.next.next = even_node
                curr_node.next = None
            return head
        