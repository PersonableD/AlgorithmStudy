import sys
sys.setrecursionlimit(10**8)
graph=[]
try:
    while True:
        n=int(input())
        graph.append(n)
except EOFError:
    pass
def binaryTree(s,e):
    if s==e:
        return
    a=s+1
    for i in range(a,e):
        if graph[s]<graph[i]:
            a=i
            break
    binaryTree(s+1,a)
    binaryTree(a,e)
    print(graph[s])
binaryTree(0,len(graph))