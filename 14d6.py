n, k = map(int, input().split())
ws = []

def check(limit):
    idx_k = 0
    idx_n = 0
    temp = 0
    array = list(ws)
    
    while True:
        if idx_k == k or idx_n == n:        
            break
        if temp + array[idx_n] <= limit:
            temp = temp + array[idx_n]
            idx_n += 1
        else:
            temp = 0
            idx_k += 1
    if idx_n < n:
        return False
    else:
        return True
        
for i in range(n):
    ws.append(int(input()))

limit = 1
left = 1
right = 100000 * 10000
mid = int((left + right) / 2)
ans = right

while left <= right:
    if check(mid):
        ans = mid
        right = mid-1
        mid  = (left + right) // 2
    else:
        left = mid+1
        mid = (left + right) // 2

print(ans)

