n = int(input())
A = list(map(int, input().split()))
x = A[-1]

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp

    return i + 1

idx = partition(A, 0, len(A) - 1)

B = []
for i in range(n):
    if i == idx:
        B.append('[' + str(x) + ']')
    else:
        B.append(str(A[i]))

print(' '.join(B))        
        
