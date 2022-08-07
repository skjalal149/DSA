
"""
######################## Binary Search Tree #########################
In the left subtree the value of node is less than or equal to its parent node
In right subtree the value of node is greater than its parent node value
"""


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None


def insertNode(bstNode, nodeValue):
    if bstNode is None:
        bstNode.data = nodeValue
    elif nodeValue <= bstNode.data:
        if bstNode.leftNode is None:
            bstNode.leftNode = BinarySearchTree(nodeValue)
        else:
            insertNode(bstNode.leftNode, nodeValue)
    else:
        if bstNode.rightNode is None:
            bstNode.rightNode = BinarySearchTree(nodeValue)
        else:
            insertNode(bstNode.rightNode, nodeValue)


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


def minValueNode(rootNode):
    current = bstNode
    while current.leftNode is not None:
        current = current.leftNode
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return  rootNode
    if nodeValue < rootNode.data:
        pass



bstNode = BinarySearchTree(40)

insertNode(bstNode, 50)
insertNode(bstNode, 70)
insertNode(bstNode, 30)
insertNode(bstNode, 20)
insertNode(bstNode, 60)
insertNode(bstNode, 10)
insertNode(bstNode, 80)
insertNode(bstNode, 90)


inOrder(bstNode)