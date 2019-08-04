n = int(input())
nums = []

for i in range(n):
    s = input()

    if s == 'deleteFirst':
        del nums[0]
    elif s == 'deleteLast':
        del nums[len(nums) - 1]
    else:
        cmd, num = s.split()
        num = int(num)

        if cmd == 'insert':
            nums.insert(0, num)
        elif cmd == 'delete':
            if num in nums:
                del nums[nums.index(num)]

print(' '.join([str(i) for i in nums]))
        
    
