import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N=int(input())
M=int(input())
parts={}
parts_m=set()
answer={}
for _ in range(M):
    X,Y,K = map(int,input().split())
    parts_m.add(X)
    if X not in parts:
        parts[X]={}
    parts[X][Y]=K
memo = {}
def assemble(num):
    if num in memo:
        return memo[num]
    if num not in parts_m:
       return {num:1}
    result = {}
    for part,count in parts[num].items():
        sub_result = assemble(part)
        for sub_part, sub_count in sub_result.items():
            result[sub_part] = result.get(sub_part,0) + sub_count *count
    memo[num] =result
    return result
answer = assemble(N)
for key,value in sorted(answer.items()):
    print(f"{key} {value}")