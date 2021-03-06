n = int(input())
nums = [input() for i in range(n)]
count = 0

def insertionSort(nums, n, g):
    count = 0
    for i in range(1, n, g):
        for j in range(0, n, g):
            if nums[i] < nums[j] and j < i:
                temp = nums[i]
                del nums[i]
                nums.insert(j, temp)
                count += 1
                break
    return count

def shellSort(nums, n):
    m = 4
    count = 0
    for i in reversed(range(1, m)):
#        insertionSort(nums, n, i)
        count += insertionSort(nums, n, i)
    return count

count = shellSort(nums, n)

print(4)
print(' '.join([str(i) for i in [1, 2, 3, 4]]))
print(count)
#print(nums)

for i in range(n):
    print(nums[i])
