class Solution:
    # def maxSubArray(self, nums):
    # lists = []
    # if len(nums) == 1:
    #     return nums[0]
    # else:
    #     for i in range(len(nums) + 1):
    #         for j in range(i+1,len(nums)+1):
    #             lists.append(sum(nums[i: j]))
    #     return max(lists)
    def maxSubArray(self, nums):
        new_num = max_total = nums[0]

        for i in range(1, len(nums)):
            new_num = max(nums[i], nums[i] + new_num)
            max_total = max(new_num, max_total)


        return max_total


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
