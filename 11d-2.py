import sys

n = int(input())
nums = [int(input()) for i in range(n)]
maxnum = - sys.maxsize
prevmax = nums[n - 1]

for i in reversed(range(n - 1)):
    dif = prevmax - nums[i]

    if dif > maxnum:
        maxnum = dif

    prevmax = max(nums[i], prevmax)

print(maxnum)
    
