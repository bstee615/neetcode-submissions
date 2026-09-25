# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find(root, n):
    # if root is None:
    #     return None
    if root.val == n.val:
        return [n]
    next_root = root.left if n.val < root.val else root.right
    return [root] + find(next_root, n)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_p = find(root, p)
        path_q = find(root, q)
        ans = []
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val:
                ans.append(path_p[i])
        return ans[-1]
