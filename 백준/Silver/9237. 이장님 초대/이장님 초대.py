import sys

input = sys.stdin.readline

N = int(input())

trees = list(map(int, input().split()))

trees.sort(reverse=True)

max_days = 0

for i in range(N):
    max_days = max(max_days, trees[i]+i+1)

print(max_days+1)
