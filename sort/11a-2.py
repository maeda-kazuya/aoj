n = int(input())
nums = list(map(int, input().split()))
ans = list(nums)

for i in range(1, n):
    v = nums[i]
    j = i - 1

    while j >= 0 and nums[j] > v:
        nums[j + 1] = nums[j]
        j -= 1


    nums[j + 1] = v
    print(nums)

print(nums)        
