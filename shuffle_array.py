class Solution:
    def restoreString(self, s, indices):
        new_string = {}
        new_list = []
        for i, j in zip(s, indices):
            new_string[j] = i
        for k in sorted(new_string):
            new_list.append(new_string[k])
        return "".join(new_list)


sol = Solution()
print(sol.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
