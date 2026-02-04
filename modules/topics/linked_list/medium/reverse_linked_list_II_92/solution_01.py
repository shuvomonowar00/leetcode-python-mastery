# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Find out the prev node of left and right node
        curr_node = head
        prev_node = None
        left_node = head
        right_node = head
        i = 1
        while curr_node:
            if i < left:
                prev_node = curr_node
            if i == left:
                left_node = curr_node
            if i == right:
                right_node = curr_node
            i += 1
            curr_node = curr_node.next
        
        # Reverse the left node to right node
        after = right_node.next
        pn = after
        cn = left_node
        while cn and cn != after:
            cnh = cn.next
            cn.next = pn
            pn = cn
            cn = cnh
        if left != 1:
            prev_node.next = pn
        else:
            head = pn

        return head


