n = int(input())
numsA = list(map(int, input().split()))
q = int(input())
numsB = list(map(int, input().split()))
count = 0

# for i in range(n):
#     for j in range(q):
#         if numsB[j] == numsA[i]:
#             count += 1
#             break

for i in range(q):
    for j in range(n):
        if numsB[i] == numsA[j]:
            count += 1
            break

print(count)            
