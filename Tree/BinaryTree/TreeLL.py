from SortingAlgorithm.StackAndQueue import Queue

class Tree:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def insertNode(tree, data):
    if not tree:
        tree = Tree(data)
    queue = Queue.Queue()
    queue.enqueue(tree)
    while not(queue.isEmpty()):
        root = queue.dequeue()
        if root.data.leftNode is not None:
            queue.enqueue(root.data.leftNode)
        else:
            root.data.leftNode = Tree(data)
        if root.data.rightNode is not None:
            queue.enqueue(root.data.rightNode)
        else:
            root.data.rightNode = Tree(data)

        
def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftNode)
    preOrder(rootNode.rightNode)


def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftNode)
    print(rootNode.data)
    inOrder(rootNode.rightNode)


def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftNode)
    postOrder(rootNode.rightNode)
    print(rootNode.data)


root = Tree("Great Grand Parent")
insertNode(root, "parent1")
insertNode(root, "parent2")

postOrder(root)