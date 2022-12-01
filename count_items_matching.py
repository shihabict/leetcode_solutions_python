class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        if ruleKey == 'type':
            for i in items:
                if i[0] == ruleValue:
                    count += 1
        elif ruleKey == 'color':
            for i in items:
                if i[1] == ruleValue:
                    count += 1
        else:
            for i in items:
                if i[2] == ruleValue:
                    count += 1
        return count


sol = Solution()
print(sol.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))
