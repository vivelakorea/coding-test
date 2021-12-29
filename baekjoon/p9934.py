K = int(input())
dfs_nodes = list(map(int, input().split()))

# root: level 0, tree[0]
# first index of kth level: 2 ** k - 1
# if index of a node is k, its children nodes are 2k + 1, 2k + 2
# if index of a node is k, and if k is even, parent node's index is k/2 - 1, and if k is odd, parent node's index is k/2 - 1/2
tree = [0] * (2 ** K - 1) 

# can go to left child: go to left
# can't go to left child: visit if not visited
    # can go to right: go to right
    # can't go to right: go to parent

tree_idx = 0
dfs_idx = 0
while dfs_idx < 2 ** K - 1:
    if 2 * tree_idx + 1 < 2 ** K - 1 and tree[2 * tree_idx + 1] == 0:
        tree_idx = 2 * tree_idx + 1
    else:
        if tree[tree_idx] == 0:
            tree[tree_idx] = dfs_nodes[dfs_idx]
            dfs_idx += 1
        if 2 * tree_idx + 2 < 2 ** K - 1 and tree[2 * tree_idx + 2] == 0:
            tree_idx = 2 * tree_idx + 2
        else:
            if tree_idx % 2 == 0:
                tree_idx = int(tree_idx / 2 - 1)
            else:
                tree_idx = int(tree_idx / 2 - 1 / 2)

for level in range(K):
    print(" ".join(str(x) for x in tree[2 ** level - 1: 2 ** (level + 1) - 1]))