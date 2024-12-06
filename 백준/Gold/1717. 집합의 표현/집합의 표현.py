import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m=map(int,input().split())
nums=[tuple(map(int,input().split())) for _ in range(m)]
parent=list(range(n+1))
def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a,b):
    a,b = find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
for choose,a,b in nums:
    if choose==0:
        union(a,b)
    if choose==1:
        if find(a)==find(b):
            print("yes")
        else:
            print("no")