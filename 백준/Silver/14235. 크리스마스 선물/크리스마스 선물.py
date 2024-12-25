import sys
import heapq
input=sys.stdin.readline
n=int(input())
gifts=[]
for _ in range(n):
    nums=list(map(int,input().split()))
    if nums[0]==0:
        if not gifts:
            print(-1)
        else:
            print(-heapq.heappop(gifts))
    else:
        for i in range(1,nums[0]+1):
            heapq.heappush(gifts,-nums[i])