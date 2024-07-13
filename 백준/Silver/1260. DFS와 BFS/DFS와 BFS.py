from collections import deque
N,M,V=map(int,input().split())
graph=[[]for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited_DFS=[False]*(N+1)
result_DFS=[]
def DFS(node,visited_DFS,result_DFS):
    visited_DFS[node]=True
    result_DFS.append(node)
    for neighbor in sorted(graph[node]):
        if not visited_DFS[neighbor]:
            DFS(neighbor,visited_DFS,result_DFS)
queue=deque()
visited_BFS=set()
result_BFS=[]
def BFS(node,visited_BFS,result_BFS):
    queue.append(node)
    visited_BFS.add(node)
    while queue:
        vertex=queue.popleft()
        result_BFS.append(vertex)
        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited_BFS:
                visited_BFS.add(neighbor)
                queue.append(neighbor)
DFS(V,visited_DFS,result_DFS)
BFS(V,visited_BFS,result_BFS)
print(*result_DFS)
print(*result_BFS)