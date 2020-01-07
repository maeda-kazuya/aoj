from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.child = []

n = int(input())
g = []

for i in range(n):
    g.append(list(map(int, input().split())))

# print(g)

for i in range(n):
    for j in range(n):
        if g[i][j] == -1:
            g[i][j] = 10**5

mst = Node(0)

def getClosestVertex(done):
    w = 10**10
    parent = None
    closest = None
    for i in done:
        for j in range(len(g[i])):
            if j in done:
                continue
            if g[i][j] < w:
                w = g[i][j]
                parent = i
                closest = j
    return parent, closest, w

# Search parent from tree and add node as child
def addChild(rootNode: Node, parentVal: int, nodeVal: int):
    if rootNode.val == parentVal:
        node = Node(nodeVal)
        rootNode.child.append(node)
    else:
        for next in rootNode.child:
            addChild(next, parentVal, nodeVal)

def bfs(rootNode: Node):
    q = deque()
    q.append(rootNode)
    while q:
        node = q.popleft()
        print(node.val)
        for next in node.child:
            q.append(next)

done = set()
done.add(0)
ans = 0
root = Node(0)


while True:
    parent, closest, w = getClosestVertex(done)
    print(parent, closest, w)
    if closest is None:
        break
    else:
        addChild(root, parent, closest)
        done.add(closest)
        ans += w

print('ans:', ans)
print('root child length:', len(root.child))
bfs(root)

'''
5
 -1 2 3 1 -1
 2 -1 -1 4 -1
 3 -1 -1 1 1
 1 4 1 -1 3
 -1 -1 1 3 -1
 '''