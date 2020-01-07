n = int(input())
nums = list(map(int, input().split()))
count = 0


while True:
    flag = 0
    
    for j in range(n - 1):    
        if (nums[j + 1] < nums[j]):
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp
            count += 1
            flag = 1
            
    if flag != 1:
        break

print(' '.join([str(i) for i in nums]))
print(count)

