import sys
input = sys.stdin.readline
N = int(input())
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)

class BinaryTree():
    def __init_(self):
        self.root = None

    def preorder(self, n):
        if n != None:
            print(chr(n.item), end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self, n):
        if n != None:
            if n.left:
                self.inorder(n.left)
            print(chr(n.item), end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self, n):
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(chr(n.item), end='')

tree = BinaryTree()
L = [0 for _ in range(27)]
for i in range(1, 27):
    L[i] = Node(64+i)
for i in range(N):
    R, l, r = map(str, input().split())
    if l != '.':
        L[ord(R)-64].left = Node(ord(l))
    if r != '.':
        L[ord(R)-64].right = Node(ord(r))

print(Node(65).left)
print(L[1].left)