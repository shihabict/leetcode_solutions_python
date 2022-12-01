class Solution:
    def maximumWealth(self, accounts):
        sum_list = []
        for acc in accounts:
            sum = 0
            for i in acc:
                sum+=i
            sum_list.append(sum)
        return max(sum_list)


sol = Solution()
print(sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))