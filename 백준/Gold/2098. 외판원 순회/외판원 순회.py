import sys
input=sys.stdin.readline
N=int(input())
costs=[list(map(int,input().split()))for _ in range(N)]
dp = [[-1]*(1<<N)for _ in range(N)]
# print((1<<N)-1)
def tsp(current,visited):
    if visited ==(1<<N)-1:
        return costs[current][0] if costs[current][0]>0 else float('inf')
    if dp[current][visited]!=-1:
        return dp[current][visited]
    
    min_cost=float('inf')
    for next in range(N):
        if visited &(1<<next) ==0 and costs[current][next]>0:
            cost = tsp(next,visited | (1<<next)) + costs[current][next]
            min_cost = min(min_cost,cost)
    
    dp[current][visited]=min_cost
    return min_cost
result = tsp(0,1)
print(result)