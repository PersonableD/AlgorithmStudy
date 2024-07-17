from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(N+1)
def virus_BFS(start):
    queue=deque([start])
    visited[start]=True
    infected=0
    while queue:
        virus=queue.popleft()
        for i in graph[virus]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                infected+=1
    return infected
print(virus_BFS(1))