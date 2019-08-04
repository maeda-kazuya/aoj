n = int(input())
numsA = list(map(int, input().split()))
m = int(input())
numsB = list(map(int, input().split()))

numsA.sort()

def sum_exist(current, target, array):
    for i in range(len(array)):
        print("\n# i: " + str(i))
        print("# current: " + str(current))
        print("# target: " + str(target))
        print("# array: " + str(array))
        
        if current == target:
            return True
        elif current + array[i] == target:
            return True
        else:
            array_next = list(array)
            del array_next[i]
            return sum_exist(current + array[i], target, array_next)
#    return False
    
# for i in range(m):
#     for j in range(n):

for i in range(m):
    if sum_exist(0, numsB[i], numsA):
        print('yes')
    else:
        print('no')        

#print(numsA)
