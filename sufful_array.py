class Solution:
    def shuffle(self, nums, n):
        new_list = []
        num1 = nums[:n]
        num2 = nums[n:]
        for i, j in zip(num1, num2):
            new_list.append(i)
            new_list.append(j)
        return new_list


sol = Solution()

print(sol.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
