n = int(input())
W = list(map(int, input().split()))
cost = 0
maxNum = 0
minNum = 100000
maxIdx = 0
minIdx = 0

while True:
#    print('# Check! W: ' + str(W))
    maxNum = -1
    minNum = 100000
    maxIdx = 0
    minIdx = 0
    
    for i in range(len(W)):
        if maxNum < W[i]:
            maxNum = W[i]
            maxIdx = i
            minNum = 100000 # If max found, reset min
        if minNum > W[i]:
            minNum = W[i]
            minIdx = i

    if minIdx > maxIdx:
        cost += W[minIdx] + W[maxIdx]        
        temp = W[minIdx]
        W[minIdx] = W[maxIdx]
        W[maxIdx] = temp
#        print('# sorted: ' + str(W))

        if minIdx == len(W)-1:
            del W[minIdx]
        if maxIdx == 0:
            del W[0]
    else:
        break

print(cost)

    

    
        
    
    
