n = int(input())
str_set = set()

for i in range(n):
    order, str = input().split()
    if order == 'insert':
        str_set.add(str)
    elif order == 'find':
        if str in str_set:
            print('yes')
        else:
            print('no')

            
            
