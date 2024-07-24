import sys
input=sys.stdin.readline
word1=[0]+list(input().strip())
word2=[0]+list(input().strip())
dp=[[0]*(len(word1)) for _ in range(len(word2))]
for i in range(1,len(word2)):
    for j in range(1,len(word1)):
        if word1[j]==word2[i]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])