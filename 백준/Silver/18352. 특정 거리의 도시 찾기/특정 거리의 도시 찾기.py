import heapq
N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
def find_city(node,graph):
    distances=[float('inf')]*(N+1)
    distances[node]=0
    queue=[(0,node)]
    while queue:
        current_distance,current_city=heapq.heappop(queue)
        if current_distance>distances[current_city]:
            continue
        for neighbor_city in graph[current_city]:
            distance=current_distance+1
            if distance<distances[neighbor_city]:
                distances[neighbor_city]=distance
                heapq.heappush(queue,(distance,neighbor_city))
    return distances
distances=find_city(X,graph)
found=False
for city in range(1,N+1):
    if distances[city]==K:
        print(city)
        found=True
if not found:
    print(-1)