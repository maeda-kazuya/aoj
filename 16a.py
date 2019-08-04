def counting_sort(A, B, k):
    C = [0] * k
    for i in range(k + 1):
        C[i] = 0

    for j in range(n + 1):
        C[A[j]] += 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i-1]

    for j in reversed(range(1, n + 1)):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

n = int(input())
A = list(map(int, input().split()))
B = [0] * len(A)

counting_sort(A, B, n)
print(B)
                
