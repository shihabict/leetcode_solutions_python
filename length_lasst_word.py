class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s:
            s = s.strip().split(' ')
            return len(s[-1])
        else:
            return 0

sol = Solution()
print(sol.lengthOfLastWord("a "))