import sys
sys.setrecursionlimit(10**6)
n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
infected=[]
def recurvsive_DFS(node,visited,infected):
    visited[node]=True
    infected.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            recurvsive_DFS(neighbor,visited,infected)
recurvsive_DFS(1,visited,infected)
print(len(infected) - 1)