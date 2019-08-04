n, k = map(int, input().split())
ws = []
limit =	n * 10000

def max_count(limit, truck_count):
    temp = 0
    for i in range(n):
        if temp	+ ws[i]	> limit:
	    temp = ws[i]
	else:
            temp += ws[i]

            
for i in range(n):
    ws.append(int(input()))


