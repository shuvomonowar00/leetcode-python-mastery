"""
    707. Design Linked List - Using Singly Linked List
"""

class MyLinkedList:
    class ListNode():
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >=self.size:
            return -1
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next
        return curr_node.val


    def addAtHead(self, val: int) -> None:
        new_head = self.ListNode(val)
        new_head.next = self.head
        self.head = new_head
        self.size += 1
        return


    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = self.ListNode(val)
            self.size += 1
            return
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = self.ListNode(val)
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index >= 0 and index <= self.size:
            if index == 0:
                self.addAtHead(val)
            elif index == self.size:
                self.addAtTail(val)
            else:
                curr_node = self.head
                j = 0
                while curr_node.next != None:
                    if j+1 == index:
                        tmp_node = curr_node.next
                        curr_node.next = self.ListNode(val)
                        curr_node.next.next = tmp_node
                        self.size += 1
                        break
                    curr_node = curr_node.next
                    j += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= 0 and index < self.size:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
                return
            curr_node = self.head
            j = 0
            while curr_node.next != None:
                if j == index-1:
                    curr_node.next = curr_node.next.next
                    self.size -= 1
                    return
                curr_node = curr_node.next
                j += 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)