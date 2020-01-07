n = int(input())
g = []

for i in range(n):
    g.append(list(map(int, input().split())))

# print(g)

for i in range(n):
    for j in range(n):
        if g[i][j] == -1:
            g[i][j] = 10**5

def getClosestVertex(done):
    w = 10**10
    closest = None
    for i in done:
        for j in range(len(g[i])):
            if j in done:
                continue
            if g[i][j] < w:
                w = g[i][j]
                closest = j
    return closest, w

done = set()
done.add(0)
ans = 0

while True:
    closest, w = getClosestVertex(done)
    if closest is None:
        break
    else:
        done.add(closest)
        ans += w

print(ans)
# print(getClosestVertex(done))


'''
5
 -1 2 3 1 -1
 2 -1 -1 4 -1
 3 -1 -1 1 1
 1 4 1 -1 3
 -1 -1 1 3 -1
'''