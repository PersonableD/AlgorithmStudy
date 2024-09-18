import sys
sys.setrecursionlimit(10**6)
N=int(input())
A=input()
graph=[[]for _ in range(N+1)]
indoor=set()
for i in range(1,N+1):
    if A[i-1]=="1":
        indoor.add(i)
for _ in range(N-1):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
count=0
for i in indoor:
    for neighbor in graph[i]:
        if neighbor in indoor:
                count+=1
visited=[False]*(N+1)
def dfs(s):
    visited[s]=True
    cnt=0
    for neighbor in graph[s]:
        if not visited[neighbor]:
            if neighbor in indoor:
                cnt+=1
            else:
                cnt+=dfs(neighbor)
    return cnt
for i in range(1,N+1):
    if i not in indoor and not visited[i]:
        num = dfs(i)
        count +=num*(num-1)
print(count)