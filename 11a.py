n = int(input())
nums = list(map(int, input().split()))
ans = []

#for i in range(1, n):
for i in range(n):
#    print('\n# i: ' + str(i))

    for j in range(n):
#        print('# j: ' + str(j))
        if nums[i] < nums[j]:
            temp = nums[i]
            del nums[i]
            nums.insert(j, temp)
            print(nums)
            break

print(nums)        
