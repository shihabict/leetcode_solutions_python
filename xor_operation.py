class Solution:
    def xorOperation(self, n, start):
        output = start
        for x in range(1, n):
            output = output ^ (start + (2 * x))
        return output


sol = Solution()
print(sol.xorOperation(4, 3))
