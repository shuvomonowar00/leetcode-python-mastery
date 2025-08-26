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
        mid_node = head
        # Find the middle node
        i = 1
        while i <= hlls:
            mid_node = mid_node.next
            i += 1
        
        sum = 0
        curr_node = head
        for i in range(hlls):
            twin_node = mid_node
            for j in range(hlls+1, lls):
                twin_node = twin_node.next
            lls -= 1
            curr_sum = curr_node.val + twin_node.val
            if sum < curr_sum:
                sum = curr_sum
            curr_node = curr_node.next
        
        return sum