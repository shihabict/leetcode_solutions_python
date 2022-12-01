class Solution:
    def plusOne(self, digits):
        num = [str(i) for i in digits]
        res = int("".join(num))
        return [i for i in str(res+1)]

sol = Solution()
print(sol.plusOne([1,2,3]))

