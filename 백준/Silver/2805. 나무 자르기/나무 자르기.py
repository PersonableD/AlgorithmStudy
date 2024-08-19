import sys
input=sys.stdin.readline
N,M = map(int,input().split())
trees=list(map(int,input().split()))
trees_max =  max(trees)
def max_cutHeight(tree_max):
    tree_min = 0
    while tree_min < tree_max :
        mid = (tree_min+tree_max+1)//2
        total=0
        for tree in trees:
            if tree>mid:
                total+=tree-mid
        if total >= M:
            tree_min=mid
        else:
            tree_max = mid-1
    return tree_min
print(max_cutHeight(trees_max))