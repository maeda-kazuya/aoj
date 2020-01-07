n = int(input())
nodes = [None] * n

class Node:
#    parent = property
    
    def __init__(self, ID, left, right):
        self.parent = -1
        self.ID = ID
        self.left = left
        self.right = right

