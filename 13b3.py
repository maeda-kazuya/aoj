n, q = map(int, input().split())
names = []
times = []
now = 0
count = 1

for i in range(n):
    name, time = input().split()
    names.append(name)
    times.append(int(time))

idx = 0
while True:
#    print('\n# count: ' + str(count))
    if (len(names) == 0):
        break

    if q < times[idx]:
        times[idx] = times[idx] - q
        now += q
        idx += 1
    else:
        now += times[idx]
        print(names[idx] + ' ' + str(now))
        del names[idx]
        del times[idx]
#        continue
    if idx == len(names):
        idx = 0

    count += 1
