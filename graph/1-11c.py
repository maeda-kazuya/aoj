from collections import deque

n = int(input())
g = []
# ans = [[-1]*n for _ in range(n)]
ans = [-1] * n
done = set()
q = deque()

for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp[2:])

# print(g)

q.append(0)
# dis = 1
ans[0] = 0
done.add(1)

while q:
    idx = q.popleft()
    adj = g[idx]
    # print('node:', idx+1)

    for i in adj:
        if i not in done:
            ans[i-1] = ans[idx] + 1
            done.add(i)
            q.append(i-1)
    # if len(adj) > 0:
    #     dis += 1

# print(ans)

for i in range(n):
    print(i+1, ans[i])

'''
4
1 2 2 4
2 1 4
3 0
4 1 3

3
1 1 2
2 1 3
3 1 1
'''