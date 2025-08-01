'''
    2095. Delete the Middle Node of a Linked List
'''
import math
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution_01:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        list_len = 0

        # Find the length of the linked list
        while curr:
            list_len += 1
            curr = curr.next
        
        # Find the middle node
        middle_node = (list_len // 2)+1 

        # Delete the node from the linked list
        if middle_node == 1:
            head = None
        else:
            curr = head
            count = 0
            while curr:
                count += 1
                if count+1 == middle_node:
                    curr.next = curr.next.next
                    break
                curr = curr.next
        
        return head


if __name__ == "__main__":
    obj = Solution_01()
    print(obj.deleteMiddle([1,3,4,7,1,2,6]))
            




        