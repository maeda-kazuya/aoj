# n = int(input())
# a = list(map(int, input().split()))

def partition(a):
    p_idx = -1
    p_val = a[p_idx]
    a1, a2 = [], []
    
    for i in range(len(a)):
        if a[i] <= p_val:
            a1.append(a[i])
        else:
            a2.append(a[i])
    for i in range(len(a1)):
        a[i] = a1[i]
    for i in range(len(a2)):
        a[i+len(a1)] = a2[i]
        
                      
    # for i in reversed(range(len(a) - 1)):
    #     if a[i] > p_val:
    #         print(i, p_idx)            
    #         print('switch!')
    #         a[i], a[p_idx] = a[p_idx], a[i]
    #         p_idx = i
    #         print(a)

a = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]

partition(a)
print(a)
            
            
            
        

    
