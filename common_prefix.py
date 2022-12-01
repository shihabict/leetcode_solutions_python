class Solution:
    def longestCommonPrefix(self, strs):
        result = []
        for s in zip(*strs):
            if len(set(s)) == 1:
                result.append(s[0])
            else:
                break

        return "".join(result)


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
