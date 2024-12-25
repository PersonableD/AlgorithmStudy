import sys
input=sys.stdin.readline
n=int(input())
gifts=[]
for _ in range(n):
    nums=list(map(int,input().split()))
    if nums[0]==0:
        if not gifts:
            print(-1)
        else:
            gifts.sort()
            print(gifts.pop())
    else:
        for i in range(1,nums[0]+1):
            gifts.append(nums[i])