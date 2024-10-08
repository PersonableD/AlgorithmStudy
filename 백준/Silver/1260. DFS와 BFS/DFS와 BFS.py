from collections import deque
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**4)
N,M,V=map(int,input().strip().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1):
    graph[i].sort()
visited_DFS=[False]*(N+1)
visited_BFS=visited_DFS.copy()
result_DFS=[]
def DFS_stack(start):
    visited_DFS[start]=True
    result_DFS.append(start)
    for i in graph[start]:
        if not visited_DFS[i]:
            DFS_stack(i)
    return result_DFS
def BFS(start):
    queue=deque([start])
    visited_BFS[start]=True
    result_BFS=[]
    while queue:
        vertex = queue.popleft()
        result_BFS.append(vertex)
        for i in graph[vertex]:
            if not visited_BFS[i]:
                queue.append(i)
                visited_BFS[i]=True
    return result_BFS
print(*DFS_stack(V))
print(*BFS(V))