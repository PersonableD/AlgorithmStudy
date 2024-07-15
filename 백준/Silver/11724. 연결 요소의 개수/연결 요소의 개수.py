import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M = map(int,input().strip().split())
graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(N+1)
count=0
def hasPath(s):
    visited[s] = True
    for neighbor in graph[s]:
        if not visited[neighbor]:
            hasPath(neighbor)
for i in range(1,N+1):
    if not visited[i]:
        hasPath(i)
        count+=1
print(count)