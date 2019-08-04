n = int(input())
X = input()
Y = input()
#dp = [[]]
dp = []

for i in range(len(X)+1):
    dp.append([])
    for j in range(len(Y)+1):
        dp[i].append(0)

for i in range(1, len(X)):
    for j in range(1, len(Y)):
        if X[i] == Y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
#print(dp[len(X)][len(Y)])
print(dp)

# def lcs(X, Y):
#     if len(X) == 0 or len(Y) == 0:
#         return 0

#     if X[-1] == Y[-1]:
#         return lcs(X[:len(X)-1]
#     for i in range(len(X)):
#         for j in range(len(Y)):
#             if

# #print(dp)
