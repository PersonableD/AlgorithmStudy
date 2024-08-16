import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
result = [-1] * N
stack = []

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)