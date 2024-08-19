import sys
input=sys.stdin.readline
N,M = map(int,input().split())
trees=list(map(int,input().split()))
trees_max =  max(trees)
def max_cutHeight(tree_min, tree_max):
    result=0
    while tree_min<= tree_max :
        mid = (tree_min+tree_max)//2
        total=0
        for tree in trees:
            if tree>mid:
                total+=tree-mid
        if total >= M:
            result=mid
            tree_min=mid+1
        else:
            tree_max = mid-1
    return result
print(max_cutHeight(0,trees_max))