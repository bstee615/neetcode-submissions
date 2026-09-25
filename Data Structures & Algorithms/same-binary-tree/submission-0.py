# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = [p]
        qq = [q]
        while len(pq) > 0 and len(qq) > 0:
            pp = pq.pop()
            qp = qq.pop()
            if pp is None:
                if qp is not None:
                    return False
                continue
            if qp is None:
                if pp is not None:
                    return False
                continue
            if pp.val != qp.val:
                return False
            pq.append(pp.left)
            pq.append(pp.right)
            qq.append(qp.left)
            qq.append(qp.right)
        if len(pq) > 0 or len(qq) > 0:
            return False
        return True
