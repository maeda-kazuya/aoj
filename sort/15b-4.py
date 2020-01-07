n = int(input())
a = list(map(int, input().split()))
cnt = 0

def merge_sort(a):
    print('sort: ' + str(a))
    if len(a) == 1:
        return
    m = len(a) // 2
    x = a[:m]
    y = a[m:]

    merge_sort(x)
    merge_sort(y)
    merge(x, y, a)
    # for i in range(len(temp)):
    #     a[i] = temp[i]

def merge(x, y, a):
    global cnt

    print('merge: ' + str(x) + ' and ' + str(y))
    #arr = []
    i = 0
    j = 0

    while i < len(x) or j < len(y):
        cnt += 1
        if i == len(x):
            #arr.append(y[j])
            a[i+j] = y[j]
            j += 1
        elif j == len(y):
            #arr.append(x[i])
            a[i+j] = x[i]
            i += 1
        elif x[i] <= y[j]:
            #arr.append(x[i])
            a[i+j] = x[i]
            i += 1
        else:
            #arr.append(y[j])
            a[i+j] = y[j]
            j += 1
    print('merged: ' + str(a))
    #return arr
    
#a = [8, 5, 9, 2, 6, 3, 7, 1, 10, 4]
merge_sort(a)

print(*a)
print(cnt)
