s = input()
# prevMax = 0
# current = 0
area = 0
lakeCount

downStack = []

for i in range(len(s)):
    if s[i] == '\\':
        downStack.append(i)
    elif s[i] == '/':
        if len(downStack) > 0:
            area += i - downStack[-1]
            del downStack[-1]

print(area)
    
