class Solution:
    def rangeSumBST(self, root, low, high):
        if root == None:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


sol = Solution()

print(sol.rangeSumBST([10, 5, 15, 3, 7, null, 18], 7, 15))
