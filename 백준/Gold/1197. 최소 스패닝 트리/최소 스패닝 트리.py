import sys
sys.setrecursionlimit(10**6)
V,E=map(int,input().split())
graph=[]
for _ in range(E):
    A,B,C=map(int,input().split())
    graph.append([A,B,C])
def kruskal(graph):
    edges= sorted(graph, key=lambda x:x[2])
    parent=list(range(V+1))
    mst=[]
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        a=find(a)
        b=find(b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
    for edge in edges:
        a,b,weight=edge
        if find(a)!=find(b):
            union(a,b)
            mst.append(edge)
    return mst
mst_weight=[]
mst = kruskal(graph)
for element in mst:
    mst_weight.append(element[2])
print(sum(mst_weight))