"""
    2130. Maximum Twin Sum of a Linked List
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lls = 2
        curr_node = head.next.next
        # Find the length of linked list
        while curr_node is not None:
            lls += 1
            curr_node = curr_node.next
        
        hlls = lls // 2
        second_half_node = head
        # Find the middle node
        i = 1
        while i < hlls:
            second_half_node = second_half_node.next
            i += 1

        prev_second_half_node = second_half_node
        second_half_node = second_half_node.next
        
        # Reverse the second half linked list
        next_node = None
        while second_half_node is not None:
            tmp_head_node = second_half_node.next
            second_half_node.next = next_node
            next_node = second_half_node
            second_half_node = tmp_head_node
        
        second_half_node = next_node
        prev_second_half_node.next = second_half_node
            
        sum = 0
        curr_node = head
        twin_node = second_half_node
        for i in range(hlls):
            curr_sum = curr_node.val + twin_node.val
            if sum < curr_sum:
                sum = curr_sum
            curr_node = curr_node.next
            twin_node = twin_node.next
        
        return sum