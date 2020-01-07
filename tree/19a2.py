pwdpwd
from collections import deque

class Node:
    def __init__(self, idx, key):
        self.idx = idx
        self.key = key
        self.parent = None        
        self.left = None
        self.right = None        

    def print_self(self):
        s = 'node {}: key = {}, '.format(self.idx + 1, self.key)
        if self.parent is not None:
            s += 'parent key = {}, '.format(self.parent)
        if self.left is not None:
            s += 'left key = {}, '.format(self.left)
        if self.right is not None:
            s += 'right key = {}, '.format(self.right)
        print(s)

n = int(input())
array = list(map(int, input().split()))
heap = []

for i in range(n):
    node = Node(i, array[i])
    heap.append(node)

for i in range(1, n):
    node = heap[i]
#    parent = heap[i // 2]
    parent = heap[(i+1) // 2 - 1]
    node.parent = parent.key
    # print('i//2: ' + str(i//2))
    # print('parent : ' + str(parent))
    if i % 2 == 1:
        parent.left = node.key
    else:
        parent.right = node.key

for i in range(n):
    node = heap[i]
    node.print_self()
    
        
        
