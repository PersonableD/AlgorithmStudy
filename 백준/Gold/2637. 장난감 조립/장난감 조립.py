import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())
parts = [[] for _ in range(N+1)]
basic_parts = set(range(1, N+1))

for _ in range(M):
    X, Y, K = map(int, input().split())
    parts[X].append((Y, K))
    if X in basic_parts:
        basic_parts.remove(X)

memo = {}

def assemble(num):
    if num in memo:
        return memo[num]
    
    if num in basic_parts:
        return {num: 1}
    
    result = {}
    for part, count in parts[num]:
        sub_result = assemble(part)
        for sub_part, sub_count in sub_result.items():
            result[sub_part] = result.get(sub_part, 0) + sub_count * count
    
    memo[num] = result
    return result

answer = assemble(N)

for key in sorted(answer.keys()):
    print(f"{key} {answer[key]}")