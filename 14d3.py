n, k = map(int, input().split())
ws = []

def check(limit):    
    print('\n#######################')
    print('# limit: ' + str(limit))
    print('#######################')
    
    idx = 0
#    bag_count = 0
    truck_count = 0
    temp = 0
    array = list(ws)
    
    while True:
        print('\n# idx: ' + str(idx))
        print('# temp: ' + str(temp))
        
        if idx == k or len(array) == 0:
            break
        
        print(str(array[0]) + 'kg!')
        
        if temp + array[0] <= limit:
            if temp == 0:
                truck_count += 1
            temp = temp + array[0]
            del array[0]

        else:
            temp = 0
            idx += 1

    # print("# bag count: " + str(bag_count))
    # return bag_count            
    print("# truck count: " + str(truck_count))
    return truck_count            

    # if len(array) > 0:
    #     print("# False: baggage is still remained..")
    #     return False
    # else:
    #     print("# True: baggage is completed!")        
    #     return True
        
for i in range(n):
    ws.append(int(input()))

limit = 1
left = 1
right = 100000 * 10000
mid = int((left + right) / 2)

# while left < right:
#     if check(mid) == k:
#         break
#     elif check(mid) < k:
#         left = mid
#         mid  = (left + right) / 2
#     elif check(mid) > k:
#         right = mid
#         mid = (left + right) / 2

# while not n == check(limit):
#     limit += 1
    
while k <= check(limit):
    limit += 1

print(limit)
#print(mid)
    

