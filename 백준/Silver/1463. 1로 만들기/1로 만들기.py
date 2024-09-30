N=int(input())
dp=[float("inf")]*(N+1)
for i in range(1,N+1):
    if i == 1 :
        dp[i]=0
    elif i%2 ==0 and i%3 ==0:
        dp[i]=min(1+dp[i//2],1+dp[i//3])
    elif i%2 ==0:
        dp[i]=min(1+dp[i//2],dp[i-1]+1)
    elif i%3 ==0:
        dp[i]=min(1+dp[i//3],dp[i-1]+1)
    else:
        dp[i] = dp[i-1]+1
print(dp[N])