class Solution:
    def searchInsert(self, nums, target):
        for i in nums:
            if i == target:
                return nums.index(i)
            elif i > target:
                return nums.index(i)
        if target>nums[-1]:
            return len(nums)

        # if target in nums:
        #     return nums.index(target)
        # else:
        #     nums.append(target)
        #     nums.sort()
        #     return nums.index(target)



sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 7))
