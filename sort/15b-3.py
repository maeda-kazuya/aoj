n = int(input())
a = list(map(int, input().split()))
cnt = 0

def merge(x, y):
    global cnt

    print('merge: ' + str(x) + ' and ' + str(y))
    arr = []
    i = 0
    j = 0

    while i < len(x) or j < len(y):
        cnt += 1
        if i == len(x):
            arr.append(y[j])
            j += 1
        elif j == len(y):
            arr.append(x[i])
            i += 1
        elif x[i] <= y[j]:
            arr.append(x[i])
            i += 1
        else:
            arr.append(y[j])
            j += 1
    print('merged: ' + str(arr))
    return arr
    
def merge_sort(a):
    print('sort: ' + str(a))
    if len(a) == 1:
        return
    m = len(a) // 2
    x = a[:m]
    y = a[m:]

    merge_sort(x)
    merge_sort(y)
    #a = merge(x, y)
    #a = list(merge(x, y))
    temp = merge(x, y)
    for i in range(len(temp)):
        a[i] = temp[i]


#test = [8, 5, 9, 2, 6, 3, 7, 1, 10, 4]
#merge_sort(test)
merge_sort(a)
print(*a)
print(cnt)
