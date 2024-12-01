import sys
input = sys.stdin.readline
N=int(input())
cards=set(input().split())
M=int(input())
ans=input().split()
for i in range(M):
    if ans[i] in cards:
        ans[i]="1"
    else:
        ans[i]="0"
print(*ans)