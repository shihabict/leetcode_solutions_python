class Solution:
    def climbStairs(self, n):
        # result = 0
        if n <= 3:
            return n
        else:
            a = 2
            b = 3
            for i in range(4,n+1):
                c = a+b
                a = b
                b = c
            return c

if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(8))
