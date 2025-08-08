"""
    707. Design Linked List - Using Doubly Linked List
"""

class ListNode():
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index == 0 and self.size > 0:
            return self.head.val
        elif index == self.size-1:
            return self.tail.val
        elif index >= 0 and index < self.size:
            curr_head = self.head
            for _ in range(index):
                curr_head = curr_head.next
            return curr_head.val
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            new_head = ListNode(val)
            new_head.prev = self.head
            new_head.next = self.tail
            self.head = new_head
            self.tail = self.head
            self.size += 1
        else:
            new_head = ListNode(val)
            new_head.prev = self.head.prev
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head
            self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        elif self.size == 1:
            new_tail = ListNode(val)
            new_tail.prev = self.head
            new_tail.next = self.tail
            self.tail = new_tail
            self.head.next = self.tail
            self.size += 1
        else:
            new_tail = ListNode(val)
            new_tail.prev = self.tail
            new_tail.next = self.tail.next
            self.tail.next = new_tail
            self.tail = new_tail
            self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > 0 and index < self.size:
            curr_node = self.head
            for _ in range(index-1):
                curr_node = curr_node.next
            new_node = ListNode(val)
            new_node.prev = curr_node
            new_node.next = curr_node.next
            curr_node.next.prev = new_node
            curr_node.next = new_node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.size == 1:
            self.head = self.head.next
            self.tail = self.head
            self.size -= 1
        elif index == 0 and self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        elif index > 0 and index == self.size-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        elif index > 0 and index < self.size-1:
            curr_node = self.head
            for _ in range(index-1):
                curr_node = curr_node.next
            curr_node.next = curr_node.next.next
            curr_node.next.prev = curr_node
            self.size -= 1





# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)