n = int(input())
nums = list(map(int, input().split()))
ans = list(nums)

#print(nums)

def printList(nums):
    print(' '.join([str(i) for i in nums]))

for i in range(1, n):
    # print('\n# i: ' + str(i))
    # print('# check position of nums[i]: {}'.format(nums[i]))

    for j in range(n):
#        print('# j: ' + str(j))        
#        print(nums)            

        if nums[i] < nums[j] and j < i:
#            print('Found bigger one!!')
#            print(nums)
            print(' '.join([str(i) for i in nums]))            
#            nums[j - 1] = nums[i]
            temp = nums[i]
            del nums[i]
#            nums.insert(j - 1, nums[i])
            nums.insert(j, temp)
            break
    else:
#        print(nums)
        print(' '.join([str(i) for i in nums]))
            
#            print(nums)
#            break
   
#print('# ans: ' + str(nums))
printList(nums)
