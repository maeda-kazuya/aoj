n = int(input())
nums = list(map(int, input().split()))
ans = list(nums)

def printList(nums):
    print(' '.join([str(i) for i in nums]))

for i in range(1, n):
    for j in range(n):
        if nums[i] < nums[j] and j < i:
            printList(nums)
            temp = nums[i]
            del nums[i]
            nums.insert(j, temp)
            break
    else:
        printList(nums)

printList(nums)
