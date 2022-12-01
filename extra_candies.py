class Solution:
    def kidsWithCandies(self, candies, extraCandies):
            max_candies = max(candies)
            result = []
            for candie in candies:
                if (candie+extraCandies)>=max_candies:
                    result.append(True)
                else:
                    result.append(False)
            return result

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))