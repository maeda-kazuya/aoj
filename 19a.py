from collections import deque

class Node:
    # parent = property
    # left = property
    # right = property

    def __init__(self, idx, key):
        self.idx = idx
        self.key = key
        self.parent = None        
        self.left = None
        self.right = None        

    def print_self(self):
#        print('node {}: key = {}, parent = {}, depth = {}, {}, '.format(self.ID, self.parent, self.depth, self.node_type) + str(self.c))
        s = 'node {}: key = {}, '.format(self.idx, self.key)
#        if parent > -1:
        if self.parent is not None:
            s += 'parent key = {}, '.format(self.parent)
        if self.left is not None:
            s += 'left key = {}, '.format(self.left)
        if self.right is not None:
            s += 'right key = {}, '.format(self.right)
        print(s)

n = int(input())
array = list(map(int, input().split()))
#heap = [None]*n
heap = []
#root = Node(0, array[0])

#for i in range(1, n):
for i in range(n):
    node = Node(i, array[i])
    heap.append(node)

print('array: ' + str(array))    
print('heap: ' + str(heap))

for i in range(1, n):
    node = heap[i]
    parent = heap[i // 2]
    node.parent = parent.key
    print('i//2: ' + str(i//2))
    print('parent : ' + str(parent))
    if i % 2 == 0:
        parent.left = node.key
    else:
        parent.right = node.key

for i in range(n):
    node = heap[i]
    node.print_self()
    
        
        
