def bubble_sort(A):
    count = 0
    for i in range(len(A)):
#        for j in reversed(range(i + 1, len(A))):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                count += 1

    print(A)
    return count

n = int(input())
A = list(map(int, input().split()))

#print(A)
print(bubble_sort(A))
