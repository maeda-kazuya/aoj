from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
colors = {}
done = set()

for i in range(m):
    s, t = map(int, input().split())
    g[s].append(t)
    g[t].append(s)

# print(g)
color = 0

for i in range(n):
    if i in colors:
        continue
    done.clear()
    color += 1
    q = deque()
    q.append(i)

    while q:
        node = q.popleft()
        colors[node] = color
        for next in g[node]:
            if next not in done:
                done.add(next)
                q.append(next)

# print(colors)

Q = int(input())
qs = []
for i in range(Q):
    s, t = map(int, input().split())
    qs.append([s, t])

for i in range(len(qs)):
    if colors[qs[i][0]] == colors[qs[i][1]]:
        print('yes')
    else:
        print('no')


'''
10 9
0 1
0 2
3 4
5 7
5 6
6 7
6 8
7 8
8 9
3
0 1
5 9
1 3
'''