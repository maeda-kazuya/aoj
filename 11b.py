import sys
a, b = map(int, input().split())

if a == b:
    print(a)
    sys.exit()

r = 0
if a > b:
    r = a % b
    a -= b
else:
    r = b % a
    b -= a
    
while True:
    print(a, b)

    if a == 0 or b == 0:
        break
    if a > b and a % b != 0:
        r = a % b
        a -= b
    elif b > a and b % a != 0:
        r = b % a
        b -= a
    else:
        break

print(r)
    
