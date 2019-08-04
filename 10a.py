# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

n = int(input())
dp = [0]*(n+1)

def calc(n):
    global dp
    for i in range(n+1):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1] + dp[i-2]

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(n))
calc(n)
print(dp[n])


