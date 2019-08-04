n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

def solve(current, target, array):
    for i in range(len(array)):
        # print("\n# i: " + str(i))
        # print("# current: " + str(current))
        # print("# target: " + str(target))
        # print("# array: " + str(array))
        
        if current == target:
            return True
        elif current + array[i] == target:
            return True
        else:
            array_next = list(array)
            del array_next[i]
            return solve(current + array[i], target, array_next) or solve(current, target, array_next)

for i in range(q):
    if solve(0, M[i], A):
        print('yes')
    else:
        print('no')        


