class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        res = []
        result_list = []
        for i in range(len(nums)):
            left_p = i + 1
            right_p = len(nums) - 1
            while left_p < right_p:
                total = nums[i] + nums[left_p] + nums[right_p]
                if total == 0:
                    result_list.append([nums[i], nums[left_p], nums[right_p]])
                    left_p += 1
                    right_p -= 1

                elif total < 0:
                    left_p += 1
                    continue
                elif total > 0:
                    right_p -= 1
                    continue

        for res_list in result_list:
            if res_list not in res:
                res.append(res_list)
        return res


if __name__ == '__main__':
    # nums = [0,0,0,0]
    nums = [-2, 0, 1, 1, 2]
    sol = Solution()
    res = sol.threeSum(nums)
    print(res)
