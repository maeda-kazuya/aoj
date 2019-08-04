n = int(input())
A = list(map(int, input().split()))
count = 0

def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [0] * n1 
    R = [0] * n2
    global count

    for i in range(n1):
        L[i] = A[left + i]
#        L.append(A[left + i])
    for i in range(n2):
        R[i] = A[mid + i]
#        R.append(A[mid + i])

    L.append(1000000000)
    R.append(1000000000)

    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            count += 1
            A[k] = L[i]
            i += 1
        else:
            count += 1            
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)

mergeSort(A, 0, len(A))
print(' '.join([str(i) for i in A]))
print(count)            
