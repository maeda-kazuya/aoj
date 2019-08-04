import sys

n = int(input())
nums = [int(input()) for i in range(n)]
maxnum = - sys.maxsize
prevmax = nums[n - 1]

# for i, num in enumerate(nums):
#     for j in range(i + 1, len(nums)):    
#         if nums[j] - nums[i] > max:
#             max = nums[j] - nums[i]

# for i in range(n - 1):
#     temp = max(nums[i+1:]) - nums[i]
#     if temp > maxnum:
#         maxnum = temp

for i in reversed(range(n - 1)):
    # print('\n# i: {}, num: {}'.format(i, nums[i]))
    # print('[Before] prevmax: ' + str(prevmax))
        
    dif = prevmax - nums[i]

#    print('dif: ' + str(dif))

    if dif > maxnum:
#        print("# update: " + str(dif))
        maxnum = dif

    prevmax = max(nums[i], prevmax)
#    print('[After] prevmax: ' + str(prevmax))

#print('prevmax: ' + str(prevmax))
print(maxnum)
    
