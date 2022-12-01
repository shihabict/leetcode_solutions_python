class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = int(str(x).strip('-')[::-1])
            n = int('-' + str(n))
        else:
            n = int(str(x)[::-1])

        if n in range(pow(-2, 31), pow(2, 31) - 1):
            return n
        else:
            return 0


sol = Solution()
print(sol.reverse(-120))
