n = int(input())
numsA = list(map(int, input().split()))
q = int(input())
numsB = list(map(int, input().split()))
count = 0

def binary_search(num, array, pointer):
    # print("\n# pointer: " + str(pointer))
    # print('array: ' + str(array))
    
    if num == array[pointer]:
#        print("# Found: " + str(num))
        return True
    elif len(array) == 1:
        return False
    elif pointer == 0:
        return False
    elif num < array[pointer]:
        # print("# Target is smaller!")
        # print("# new array: " + str(array[:pointer]))
        return binary_search(num, array[:pointer], int(len(array[:pointer]) / 2))
    elif num > array[pointer]:
        # print("# Target is bigger!")
        # print("# new array: " + str(array[pointer:]))
#        return binary_search(num, array[pointer:], int(len(array[pointer:]) / 2))
        return binary_search(num, array[pointer+1:], int(len(array[pointer+1:]) / 2))        
    
for i in range(q):
    if binary_search(numsB[i], numsA, int(len(numsA) / 2)):
        count += 1

print(count)            
