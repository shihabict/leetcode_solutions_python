class Solution:
    def numJewelsInStones(self, jewels, stones):
        result = 0
        for st in stones:
            if st in jewels:
                result += 1
        return result


sol = Solution()
print(sol.numJewelsInStones('z', 'ZZ'))
