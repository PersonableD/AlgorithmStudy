import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i // 2], dp[i // 3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i - 1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3], dp[i - 1]) + 1
    else:
        dp[i] = dp[i - 1] + 1

print(dp[N])