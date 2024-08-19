import sys
input = sys.stdin.readline
def max_cutHeight(trees, M):
    if M == 0:
        return max(trees)
    tree_heights = sorted(trees, reverse=True)
    total = sum(tree_heights)
    if total == M:
        return 0
    cumulative_sum = 0
    for i in range(len(tree_heights) - 1):
        cumulative_sum += (tree_heights[i] - tree_heights[i+1]) * (i + 1)
        if cumulative_sum >= M:
            return tree_heights[i+1] + (cumulative_sum - M) // (i + 1)
    return (total - M) // len(trees)
N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(max_cutHeight(trees, M))