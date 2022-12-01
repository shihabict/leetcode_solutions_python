class Solution:
    def twoSum(self, numbers, target):
        left_p = 0
        right_p = len(numbers) - 1
        while left_p < right_p:
            if numbers[left_p]+numbers[right_p]>target:
                right_p-=1
                continue
            if numbers[left_p]+numbers[right_p]<target:
                left_p+=1
                continue
            elif numbers[left_p]+numbers[right_p]==target:
                break
        return [left_p+1,right_p+1]

if __name__ == '__main__':
    # nums = [2,7,11,15]
    # target = 9
    # nums = [2, 3, 4]
    # target = 6
    # nums = [-1,0]
    # target = -1
    nums = [5, 25, 75]
    target = 100
    sol = Solution()
    res = sol.twoSum(nums, target)
    print(res)
