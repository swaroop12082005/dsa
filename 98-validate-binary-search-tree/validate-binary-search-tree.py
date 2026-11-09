class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):

            # If node does not exist, return True
            if not node:
                return True

            # Check whether the current node is within the allowed range
            if not (node.val < right and node.val > left):
                return False

            # Check the left and right subtrees
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        # Start checking from the root
        # Initially, there is no minimum or maximum limit
        return valid(root, float("-inf"), float("inf"))





