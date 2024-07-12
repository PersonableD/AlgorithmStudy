import sys
sys.setrecursionlimit(10**8)
N=int(input())
tree={}
parent={}
for i in range(N):
    root,point_one,point_two=input().split()
    tree[root]=(point_one,point_two,root)
    if point_one !='.':
        parent[point_one]=root
    if point_two !='.':
        parent[point_two]=root
def preorder(start):
    if start!='.':
        print(start,end="")
        preorder(tree[start][0])
        preorder(tree[start][1])
def inorder(start):
    if start!='.':
        inorder(tree[start][0])
        print(start,end="")
        inorder(tree[start][1])
def postorder(start):
    if start!='.':
        postorder(tree[start][0])
        postorder(tree[start][1])
        print(start,end="")
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()