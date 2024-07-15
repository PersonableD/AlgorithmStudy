from collections import deque
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N,M = map(int,input().strip().split())
graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
def hasPath(s):
    queue=deque([s])
    visited[s]=True
    while queue:
        vertex=queue.popleft()
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
visited=[False]*(N+1)
count=0
for i in range(1,N+1):
    if not visited[i]:
        hasPath(i)
        count+=1
print(count)