class TreeList:
    def __init__(self, size):
        self.custom = size * [None]
        self.lastUpdatedIndex = 0
        self.maxSize = size

    def __iter__(self):
        for i in self.custom:
            yield i

    def __str__(self):
        ls = [str(x) for x in self.custom]
        return " ".join(ls)

    def insertNode(self, value):
        if self.lastUpdatedIndex +1 == self.maxSize:
            return "Binary Tree is Full"
        self.custom[self.lastUpdatedIndex+1] = value
        self.lastUpdatedIndex += 1
        return "data inserted"



newTL = TreeList(8)
newTL.insertNode(2)
newTL.insertNode(2)
newTL.insertNode(2)
newTL.insertNode(2)
newTL.insertNode(2)
newTL.insertNode(2)
newTL.insertNode(2)
newTL.insertNode(2)
print(newTL)