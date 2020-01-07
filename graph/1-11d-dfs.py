import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    s, t = map(int, input().split())
    g[s].append(t)
    g[t].append(s)

# print(g)

q = int(input())
qs = []
for i in range(q):
    s, t = map(int, input().split())
    qs.append([s, t])

# print(qs)
done = set()

def solve(s, t):
    # print(s, t)
    ans = False
    if t in g[s]:
        done.add(s)
        return True
    else:
        # print(g[s])
        for adj in g[s]:
            # print('adj:', adj)
            if adj not in done:
                done.add(adj)
                # return solve(adj, t)
                ans = ans or solve(adj, t)

    return ans
    # return False

for temp in qs:
    done.clear()

    # DEBUG
    # if temp != [0,9]:
    #     continue

    if solve(temp[0], temp[1]):
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