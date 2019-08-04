n, q = map(int, input().split())
names = []
times = []
now = 0
#count = 1

for i in range(n):
    name, time = input().split()
    names.append(name)
    times.append(int(time))

#print(times)

while True:
#    print('\n# count: ' + str(count))
    isAllDone = True
    
    for i in range(n):
        if names[i] == 'done':
            continue
        else:
            isAllDone = False
        
        if q < times[i]:
            times[i] = times[i] - q
            now += q
        # elif q == times[i]:
        #     now += q
        #     print(names[i] + ' ' + str(now))
        #     names[i] = 'done'
        else:
            now += times[i]
            print(names[i] + ' ' + str(now))
            names[i] = 'done'            
    if (isAllDone):
        break

        
    # isAllDone = True
    # for i in range(n):
    #     if names[i] != 'done':
    #         isAllDone = False
        


