from collections import deque
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
points=[0 for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    points[b]+=1
result=[]
queue=deque()
def topological_sorting():
    for i in range(1,N+1):
        if points[i]==0:
            queue.append(i)
    while  queue:
        vertex=queue.popleft()
        result.append(vertex)
        for i in graph[vertex]:
            points[i]-=1
            if points[i]==0:
                queue.append(i)
topological_sorting()
print(*result)