import sys
sys.setrecursionlimit(10**6)
N=int(input())
A=input()
graph=[[]for _ in range(N+1)]
indoor=[]
for _ in range(N-1):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,len(A)+1):
    if A[i-1]=="1":
        indoor.append(i)
count=0
def dfs(s):
    global count
    visited[s]=True
    for neighbor in graph[s]:
        if not visited[neighbor]:
            if neighbor in indoor:
                count+=1
            else:
                dfs(neighbor)
for i in range(len(indoor)):
    visited=[False]*(N+1)
    dfs(indoor[i])
print(count)