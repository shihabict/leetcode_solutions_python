class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        res = []
        result_list = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left_p = j + 1
                right_p = len(nums) - 1
                while left_p < right_p:

                    total = nums[i] + nums[j] + nums[left_p] + nums[right_p]
                    print(f"{nums[i]}, {nums[j]}, {nums[left_p]}, {nums[right_p]} ----- > {total}")
                    if total == target:
                        result_list.append([nums[i], nums[j], nums[left_p], nums[right_p]])
                        left_p += 1
                        right_p -= 1

                    if total < target:
                        left_p += 1

                    if total > target:
                        right_p -= 1

        for res_list in result_list:
            if res_list not in res:
                res.append(res_list)
        return res


if __name__ == '__main__':
    # nums = [1, 0, -1, 0, -2, 2]
    # target = 0
    nums = [2, 2, 2, 2, 2]
    target = 8
    sol = Solution()
    sol.fourSum(nums, target)
