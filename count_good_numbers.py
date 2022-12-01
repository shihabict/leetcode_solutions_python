class Solution:
    def countGoodNumbers(self, n):
        m = int(n / 2)
        if n % 2 == 0:
            result = pow(20, m, 10 ** 9 + 7)
        else:
            result = pow(20, m, 10 ** 9 + 7) * 5
        return int(result % (pow(10, 9) + 7))


sol = Solution()
print(sol.countGoodNumbers(50))
