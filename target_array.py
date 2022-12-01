class Solution:
    def createTargetArray(self, nums, index):
        t_array = []
        for i, j in zip(index, nums):
            t_array.insert(i, j)
        return t_array


sol = Solution()
print(sol.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
