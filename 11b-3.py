a, b = map(int, input().split())

def gcdOld(x, y):
    while y != 0:
        x, y = y, x%y
    return x, y

def gcd(a, b):
    dividend = max(a, b)
    divider = min(a, b)

    if divider == 0:
        return dividend
    
    while dividend % divider != 0:
        r = dividend % divider
        dividend = divider
        divider = r
        #dividend, divider = divider, dividend % divider
    return divider

#dividend, divider = max(a, b), min(a, b)
#r = dividend % divider
#divider = min(a, b)

# while dividend % divider != 0:
#     r = dividend % divider
#     dividend = divider
#     divider = r
#print(r)

#print(gcdOld(20, 0))
print(gcd(a, b))


