n = int(input())
g = []
ans1 = []
done = set()
time = 0

for i in range(n):
    temp = list(map(int, input().split()))
    g.append(temp[2:])

print(g)

def traverse(idx):
    global time
    if idx > n-1:
        return
    if idx in done:
        return

    time += 1
    adj = g[idx]
    ans1.append(time)
    done.add(idx)

    for i in adj:
        traverse(i-1)

# def traverse(idx, time):
#     if idx > n-1:
#         return
#     if idx in done:
#         return
#
#     adj = g[idx]
#     ans1.append(time+1)
#     done.add(idx)
#
#     for i in adj:
#         traverse(i-1, time+1)

traverse(0)
print(ans1)



'''
6
1 2 2 3
2 2 3 4
3 1 5
4 1 6
5 1 6
6 0


4
1 1 2
2 1 4
3 0
4 1 3
'''