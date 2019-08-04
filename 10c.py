n = int(input())

def solve(X, Y, Z):
    i = 0
    j = 0

    # if len(X) == 0 or len(Y) == 0:
    #     return Z

    while True:
        print('\n ----------------')
        print('# i: ' + str(i))
        print('# j: ' + str(j))        
        print('# X: ' + X)
        print('# Y: ' + Y)

        if i >= len(X) or j >= len(Y):
            break
        
        x = X[i]
        y = Y[j]

        if x == y:
            i += 1
            j += 1
            Z += x
            continue
        else:
            Z1 = solve(X[i+1:], Y, Z)
            Z2 = solve(X, Y[j+1:], Z)
            if (len(Z1) > len(Z2)):
                i += 1
                Z += Z1
            else:
                j += 1
                Z += Z2
            
    return Z
    
# for i in range(n):
#     X = input()
#     Y = input()

#     Z = solve(X, Y, '')
#     print(Z)

X = input()
Y = input()
Z = solve(X, Y, '')
print(Z)

