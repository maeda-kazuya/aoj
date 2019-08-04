s = list(input().split())
stack = []
 
for i in range(len(s)):
    if s[i] == '+':
        stack.append(stack.pop() + stack.pop())
    elif s[i] == '-':
        stack.append(-(stack.pop() - stack.pop()))
    elif s[i] == '*':
        stack.append(stack.pop() * stack.pop())
    else:
        stack.append(int(s[i]))
 
#print(stack.pop())
print(stack[-1])
