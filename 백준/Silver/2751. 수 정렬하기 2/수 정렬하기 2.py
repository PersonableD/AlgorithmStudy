import sys
input=sys.stdin.readline
N=int(input())
nums=[int(input()) for _ in range(N)]
nums=sorted(nums)
for num in nums:
    print(num)