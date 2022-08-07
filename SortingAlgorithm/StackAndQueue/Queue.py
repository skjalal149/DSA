from SortingAlgorithm.LinkedList import SingleLinkedList


class QueueLL:

    def __init__(self):
        self.LinkedList = SingleLinkedList.SingleLinkedList()

    def __str__(self):
        x = [str(i.value) for i in self.LinkedList]
        return " ".join(x)

    def enqueue(self, value):
        newNode = SingleLinkedList.Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        return True if self.LinkedList.head is None else False

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        tempNode = self.LinkedList.head
        if self.LinkedList.head == self.LinkedList.tail:
            self.LinkedList.head = None
            self.LinkedList.tail = None
        else:
            self.LinkedList.head = self.LinkedList.head.next
        return tempNode

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.LinkedList.head



class Queue:
    def __init__(self, max_length=0):
        self.queue = []
        self.max_length = max_length

    def enqueue(self, data):
        n = len(self.queue)
        if self.max_length != 0 and n >= self.max_length:
            return ("Queue is full")
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[len(self.queue) - 1]

    def isEmpty(self):
        n = len(self.queue)
        if n <= 0:
            return True
        return False

    def deleteQueue(self):
        self.queue = []

    def isFull(self) -> bool:
        n = len(self.queue)
        if n >= self.max_length:
            return True
        return False

    def __str__(self):
        ret = ""
        if self.isEmpty():
            return "No data in Queue"
        for i in range(len(self.queue)):
            ret += str(self.queue[i]) + ","
        return ret


class CircularQueue:
    def __init__(self):
        self.queue = []
        self.start = 0
        self.end = 1

    def enqueue(self, data):
        n = len(self.queue)
        if self.max_length != 0 and n >= self.max_length:
            return ("Queue is full")
        self.queue.append(data)
        self.end += 1

    def dequeue(self):
        self.start += 1
        return self.queue.pop(0)

    def peek(self):
        return self.queue[len(self.queue) - 1]

    def isEmpty(self):
        n = len(self.queue)
        if n <= 0:
            return True
        return False

    def deleteQueue(self):
        self.queue = []

    def isFull(self) -> bool:
        n = self.start - self.end
        if n == 1:
            return True
        return False

    def __str__(self):
        ret = ""
        if self.isEmpty():
            return "No data in Queue"
        for i in range(len(self.queue)):
            ret += str(self.queue[i]) + ","
        return ret
