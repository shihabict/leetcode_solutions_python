class Solution:
    def maxDepth(self, s: str) -> int:
        result = count = 0
        for c in s:
            if c == '(':
                count += 1
                result = max(result, count)
            elif c == ')':
                count -= 1
        return result

sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))