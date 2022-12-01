class Solution:
    def maxProductDifference(self, nums):
        nums = sorted(nums,reverse=False)[::-1]
        # nums = nums[::-1]
        w,x,y,z = nums[0],nums[1],nums[-2],nums[-1]
        return (w*x)-(y*z)



sol = Solution()
print(sol.maxProductDifference([4,2,5,9,7,4,8]))