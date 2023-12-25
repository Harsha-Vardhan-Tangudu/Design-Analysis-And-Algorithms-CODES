def rook(n):
    for i in range(n):
        for j in range(n):
            dp[i][j]=0
    for i in range(n):
        dp[1][0]=1
        dp[0][1]=1
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]


    return dp[n-1][n-1]
