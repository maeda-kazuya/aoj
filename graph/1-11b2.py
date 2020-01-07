from collections import deque

n = int(input())
g = []
ans1 = []
done = set()
time = 0
s = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp[2:])

print(g)

def addToStack(idx):
    if idx > n-1:
        return
    if idx in done:
        return

    s.append(idx+1)
    done.add(idx)
    adj = g[idx]

    for i in adj:
        addToStack(i-1)

def popFromStack():
    while s:
        idx = s.pop()
        print(idx)

addToStack(0)
print(s)
popFromStack()



'''
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0
'''