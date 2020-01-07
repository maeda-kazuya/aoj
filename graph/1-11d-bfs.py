from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n)]
done = set()

for i in range(m):
    s, t = map(int, input().split())
    g[s].append(t)
    g[t].append(s)

print(g)

Q = int(input())
qs = []
for i in range(Q):
    s, t = map(int, input().split())
    qs.append([s, t])

ans = [None]*Q
# for ques in qs:
for i in range(len(qs)):
    done.clear()
    q = deque()
    q.append(qs[i][0])
    # done.add(qs[i][0])
    target = qs[i][1]

    while q:
        node = q.popleft()
        if target in g[node]:
            ans[i] = 'yes'
            break
        else:
            for next in g[node]:
                if next not in done:
                    done.add(next)
                    q.append(next)
    if ans[i] is None:
        ans[i] = 'no'

# print(ans)

for text in ans:
    print(text)


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