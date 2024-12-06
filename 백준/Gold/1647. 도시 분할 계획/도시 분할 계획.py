import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
V,E=map(int,input().strip().split())
edges= sorted([tuple(map(int,input().strip().split())) for _ in range(E)], key=lambda x:x[2])
parent=list(range(V+1))
mst_weight = []
edge_count=0
for a,b,weight in edges:
    if find(a)!=find(b):
        union(a,b)
        mst_weight.append(weight)
        edge_count+=1
        if edge_count==V-1:
            break
max_num=max(mst_weight)
mst_weight.remove(max_num)
print(sum(mst_weight))