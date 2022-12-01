# bcabc
class Solution:
    def removevDuplicateLetter(self, s):
        lookup = []
        lookup.append(s[0])
        for i in range(1, len(s)):
            if s[i] not in lookup:
                lookup.append(s[i])
        for j in range(len(lookup)):
            for k in range(len(lookup)):
                if lookup[j]<lookup[k]:
                    temp = lookup[j]
                    lookup[j] = lookup[k]
                    lookup[k] = temp

        return ''.join(lookup)



sol = Solution()
print(sol.removevDuplicateLetter('bcabc'))
# if 'b'<'c':
#     print('b')
