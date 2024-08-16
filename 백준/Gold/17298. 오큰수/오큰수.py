import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
result = [-1] * N
stack = []

# 배열을 거꾸로 순회합니다
for i in range(N - 1, -1, -1):
    # 현재 숫자보다 작은 수는 스택에서 제거합니다
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    
    # 스택이 비어있지 않다면, 스택의 top이 오큰수입니다
    if stack:
        result[i] = stack[-1]
    
    # 현재 숫자를 스택에 추가합니다
    stack.append(nums[i])

print(*result)