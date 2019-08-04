n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

def solve(idx, current, target):
        # print("\n# i: " + str(i))
        # print("# current: " + str(current))
        # print("# target: " + str(target))
        # print("# array: " + str(array))
    if current > target:
        return False
    elif len(A) == idx:
        return False
    elif current + sum(A[idx:]) < target:
        return False
    elif current == target:
        return True
    elif current + A[idx] == target:
        return True
    else:
        return solve(idx + 1, current + A[idx], target) or solve(idx + 1, current, target)

for i in range(q):
    if solve(0, 0, M[i]):
        print('yes')
    else:
        print('no')        


