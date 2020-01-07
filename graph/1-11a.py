n = int(input())
adj = []
# adj = [[None] * n for _ in range(n)]
ans = [[0] * n for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    if len(temp) > 2:
        adj.append(temp[2:])
    else:
        adj.append([])

# print(adj)
# print(ans)

for i in range(n):
    for j in range(len(adj[i])):
        ans[i][adj[i][j]-1] = 1

# print(ans)

for i in range(n):
    print(*ans[i])



'''
4
1 2 2 4
2 1 4
3 0
4 1 3
'''