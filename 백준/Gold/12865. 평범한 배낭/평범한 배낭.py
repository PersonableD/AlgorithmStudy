import sys
input=sys.stdin.readline
N,K=map(int,input().split())
w=[0]
v=[0]
dp=[[0]*(K+1) for _ in range(N+1)]
for _ in range(N):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)
for i in range(1,N+1):
    for j in range(1,K+1):
        if w[i]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[N][K])