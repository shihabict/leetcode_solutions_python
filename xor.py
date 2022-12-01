class Solution:
    def decode(self, encoded, first):
        arr = [first]
        for i in encoded:
            arr.append(i ^ arr[-1])
        return arr


sol = Solution()

print(sol.decode([1, 2, 3], 1))
