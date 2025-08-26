"""
    206. Reverse Linked List
"""
from typing import Optional

class Solution_01:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_tmp_node = None
        while head != None:
            tmp_node = head.next
            head.next = tmp_tmp_node
            tmp_tmp_node = head
            head = tmp_node
        return tmp_tmp_node