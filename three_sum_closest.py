class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        res = 0
        prev_diff = float('inf')
        for i in range(len(nums) - 2):
            left_p = i + 1
            right_p = len(nums) - 1
            while left_p < right_p:
                total = nums[i] + nums[left_p] + nums[right_p]
                diff_val = abs(target - total)
                if total == target:
                    return total
                if abs(prev_diff) > diff_val:
                    res = total
                prev_diff = min(prev_diff, diff_val)

                if total > target:
                    right_p -= 1
                else:
                    left_p += 1

        return res


if __name__ == '__main__':
    # nums = [0,0,0]
    nums = [1, 1, 1, 0]
    # nums = [-1, 2, 1, -4]
    target = -100
    sol = Solution()
    res = sol.threeSumClosest(nums, target)
    print(res)
