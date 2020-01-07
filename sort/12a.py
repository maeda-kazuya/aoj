n = int(input())
nums = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i + 1, n):
        if (nums[j] < nums[i]):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            count += 1

print(' '.join([str(i) for i in nums]))            
print(count)

