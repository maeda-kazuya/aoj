n = int(input())

for k in range(n):
    X = input()
    Y = input()
    # dp = [[0 for i in range(len(Y))] for j in range(len(X))]
    dp = [[0] * len(Y) for _ in range(len(X))]
    # dp = []

    # for i in range(len(X)):
    #     dp.append([])
    #     for j in range(len(Y)):
    #         dp[i].append(0)

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
            else:
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[len(X)-1][len(Y)-1])
    #print(dp)

