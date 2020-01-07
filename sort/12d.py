n = int(input())
nums = [input() for i in range(n)]
count = 0

def insertionSort(nums, n, g):
    for i in range(g, n):
        v = nums[i]
        j = i - g

        while j >= 0 and 

