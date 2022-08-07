class Stack:
    def __init__(self):
        self.lst = []

    def push(self, value):
        self.lst.append(value)

    def pop(self):
        if len(self.lst) >= 1:
            return self.lst.pop()
        return "stack is empty"

    def peek(self):
        n = len(self.lst)
        if n >= 1:
            return self.lst[n-1]
        return "stack is empty"

    def isEmpty(self):
        if not self.lst:
            return True
        return False

    def isFull(self):
        pass

    def delete(self):
        self.lst = None
        