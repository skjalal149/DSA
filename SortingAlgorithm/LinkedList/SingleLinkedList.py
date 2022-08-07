
class Node:
    def __init__(self, value=None):
        self.value= value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node =node.next

    def insertValue(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail= newNode

    def searchValue(self, value):
        node = self.head
        index = 0
        while node != None:
            if node.value == value:
                return index
            index +=1
            node = node.next
        return "not found"

    def deleteVale(self, location):
        if self.head is None:
            return "No linkedlist created"
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is None:
                    if self.head == self.node:
                        break
                    node = node.next
                node.next = None
                self.tail = node
        else:
            index = 0
            prevNode = self.head
            while index < location-1:
                prevNode = prevNode.next
                index +=1
            nextNode = prevNode.next
            prevNode.next = nextNode.next


    def print(self):
        if self.head is None:
            print("No Single linked list exist")
        else:
            node = self.head
            while node != None:
                print(f"{node.value}")
                node = node.next

