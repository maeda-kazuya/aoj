n, k = map(int, input().split())
ws = []

def check(limit):
    print('\n#######################')
    print('# limit: ' + str(limit))
    print('#######################')
    
    idx_k = 0
    idx_n = 0
    temp = 0
    array = list(ws)
    
    while True:
        print('\n# idx_k: ' + str(idx_k))
        print('# temp: ' + str(temp))
        if idx_k == k or idx_n == n:        
            break
        print(str(array[idx_n]) + 'kg!')
        if temp + array[idx_n] <= limit:
            temp = temp + array[idx_n]
            idx_n += 1
        else:
            temp = 0
            idx_k += 1
    if idx_n < n:
        print("# False: baggage is still remained..")
        return False
    else:
        print("# True: baggage is completed!")        
        return True
        
for i in range(n):
    ws.append(int(input()))

limit = 1
left = 1
right = 100000 * 10000
mid = int((left + right) / 2)
ans = right

#while left + 1 < right:
while left <= right:
    print("# left: " + str(left))
    print("# mid: " + str(mid))        
    print("# right: " + str(right))    
    if check(mid):
        ans = mid
        right = mid-1
        mid  = (left + right) // 2
    else:
        left = mid+1
        mid = (left + right) // 2

#print(right)        
#print(mid + 1)
#print(mid)
print(ans)

    

