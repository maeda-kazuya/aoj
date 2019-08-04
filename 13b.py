n, q = map(int, input().split())
names = []
times = []
now = 0
count = 1
for i in range(n):
    name, time = input().split()
    names.append(name)
    times.append(int(time))

#print(times)

while True:
#    print('\n# count: ' + str(count))
    
    for i in range(n):
        if names[i] == 'done':
            continue
        
        if q < times[i]:
            times[i] = times[i] - q
            now += q
        elif q == times[i]:
            now += q
            print(names[i] + ' ' + str(now))
            names[i] = 'done'
            # del names[i]
            # del times[i]
        else:
            now += times[i]
            print(names[i] + ' ' + str(now))
            names[i] = 'done'            
            # del names[i]
            # del times[i]

    isAllDone = True
    for i in range(n):
        if names[i] != 'done':
            isAllDone = False

    if (isAllDone):
        break

    count += 1
        
        


