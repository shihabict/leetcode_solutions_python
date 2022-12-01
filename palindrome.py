class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x < 0:
        #     return 'false'
        # else:
        #     return str(x) == str(x)[::-1]
        if x < 0:
            return False

        input_num = x
        num = 0
        while x > 0:
            num = num * 10 + x % 10
            x = x // 10
        return num == input_num

sol = Solution()
print(sol.isPalindrome(121))

