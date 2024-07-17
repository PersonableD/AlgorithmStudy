import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input())
graph={}
for i in range(N):
    a,b,c=input().split()
    graph[a]=(b,c)
def preorder(start):
    if start!=".":
        print(start,end="")
        preorder(graph[start][0])
        preorder(graph[start][1])
def inorder(start):
    if start!=".":
        inorder(graph[start][0])
        print(start,end="")
        inorder(graph[start][1])
def postorder(start):
    if start!=".":
        postorder(graph[start][0])
        postorder(graph[start][1])
        print(start,end="")
preorder("A")
print()
inorder("A")
print()
postorder("A")