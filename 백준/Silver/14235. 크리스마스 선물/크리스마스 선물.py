import sys
import heapq
input=sys.stdin.readline
n=int(input())
gifts=[]
for _ in range(n):
    nums=list(map(int,input().split()))
    if nums[0]==0:
        if gifts:
            print(-heapq.heappop(gifts))
        else:
            print(-1)
    else:
        for gift in nums[1:]:
            heapq.heappush(gifts,-gift)