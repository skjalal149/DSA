class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def insertNode(self,value, location):
        node = Node(value)
        if not self.head:
            node.next = node
            self.head = node
            self.tail = node
        elif location == 0:
            node.next = self.head
            self.head = node
            self.tail.next = node
        elif location == -1:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location -1:
                tempNode = tempNode.next
                index += 1
            node.next = tempNode.next
            tempNode.next = node

    def traverseCSLL(self):
        if self.head is None:
            print("No node present")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode= tempNode.next
                if tempNode == self.tail.next:
                    print(self.tail.next)
                    print(tempNode)
                    break



circular_single_linkedlist = CircularSingleLinkedList()
circular_single_linkedlist.insertNode(10, 0)
circular_single_linkedlist.insertNode(11, 0)
circular_single_linkedlist.insertNode(12, 0)
circular_single_linkedlist.insertNode(13, 1)
circular_single_linkedlist.insertNode(14, -1)
circular_single_linkedlist.insertNode(15, 2)
circular_single_linkedlist.insertNode(16, 3)
circular_single_linkedlist.insertNode(17,3)
circular_single_linkedlist.traverseCSLL()