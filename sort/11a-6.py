n = int(input())
a = list(map(int, input().split()))
print(*a)

def insertion_sort(a):
    for i in range(len(a)-1):
        #l =  i
        #j = l + 1
        j = i + 1    

        while i >= 0:
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]

                i -= 1
                j -= 1
            else:
                break
        
        # while l >= 0:
        #     if a[j] < a[l]:
        #         a[l], a[j] = a[j], a[l]

        #         l -= 1
        #         j -= 1
        #     else:
        #         break
        print(*a)

insertion_sort(a)
print(a)
