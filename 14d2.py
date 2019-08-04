n, k = map(int, input().split())
ws = []

#def isok(limit, array):
def isok(limit, ws):
    print('\n#######################')
    print('# limit: ' + str(limit))
    print('#######################')
    
    idx = 0
    temp = 0
    array = list(ws)
    
    while True:
#        print('\n# k: ' + str(k))        
        print('\n# idx: ' + str(idx))
        print('# temp: ' + str(temp))
        
        if idx == k or len(array) == 0:
            break

        print(str(array[0]) + 'kg!')
        if temp + array[0] <= limit:
            temp = temp + array[0]
            del array[0]
        else:
            temp = 0
            idx += 1

    if len(array) > 0:
        print("# False: baggage is still remained..")
        return False
    else:
        print("# True: baggage is completed!")        
        return True
        
for i in range(n):
    ws.append(int(input()))

limit = 1

while not isok(limit, ws):
    limit += 1

print(limit)    
    

