n = int(input())
nodes = [None] * n
rootIdx = None

class Node:
    parent = property
    sibling = property
    node_type = property
    depth = property
    height = property
    
    def __init__(self, ID, left, right):
        self.parent = -1
        self.sibling = -1
        self.ID = ID
        self.left = left
        self.right = right

    def print_self(self):
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}, '
              .format(self.ID, self.parent, self.sibling, self.deg(), self.depth, self.height, self.node_type))

    def deg(self):
        if self.left > -1 and self.right > -1:
            return 2
        elif self.left > -1 or self.right > -1:
            return 1
        else:
            return 0

# Set depth        
def setDepth(node, depth):
    node.depth = depth
    if node.left > -1:
        left = nodes[node.left]
        setDepth(left, depth + 1)
    if node.right > -1:
        right = nodes[node.right]
        setDepth(right, depth + 1)

def getHeight(node, current):
    if node.left == -1 and node.right == -1:
        return current
    leftMax = current
    rightMax = current
    if node.left > -1:
        leftMax = getHeight(nodes[node.left], current + 1)
    if node.right > -1:
        rightMax = getHeight(nodes[node.right], current + 1)

    return max(leftMax, rightMax)

# Load nodes            
for i in range(n):
    s = list(map(int, input().split()))
    ID = s[0]
    left = s[1]
    right = s[2]
    node = Node(ID, left, right)
    nodes[ID] = node

# Set parent
for i in range(n):
    node = nodes[i]
    if node.left > 0:
        left = nodes[node.left]
        left.parent = node.ID
    if node.right > 0:
        right = nodes[node.right]
        right.parent = node.ID

# Find root index
for i in range(n):
    node = nodes[i]
    if node.parent == -1:
        rootIdx = node.ID

setDepth(nodes[rootIdx], 0)
height = getHeight(nodes[rootIdx], 0)

for i in range(n):
    node = nodes[i]
    node.height = height - node.depth

    if node.parent == -1:
        node.node_type = 'root'
    elif node.left > -1 or node.right > -1:
        node.node_type = 'internal node'        
    else:
        node.node_type = 'leaf'        

for i in range(n):
    nodes[i].print_self()
        

