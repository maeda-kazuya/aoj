n = int(input())
a = list(map(int, input().split()))
print(*a)

for i in range(len(a)-1):
    l = i
    j = l + 1    
    
    while l >= 0:
        if a[j] < a[l]:
            temp = a[l]
            a[l] = a[j]
            a[j] = temp

            l -= 1
            j -= 1
        else:
            break
    print(*a)

            
        

    
