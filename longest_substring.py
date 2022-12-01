class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sub_string = []
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s) + 1):
        #         sub = s[i:j]
        #         print(sub, end=" ")
        #         if s[i] not in sub[1:]:
        #             sub_string.append(sub)
        #         # print(s[i:j], end=" ")
        #     print()
        # return sub_string
        if len(s) == 0:
            return 0
        map = {}
        max_length = start = 0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            map[s[i]] = i
        return max_length


sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))
