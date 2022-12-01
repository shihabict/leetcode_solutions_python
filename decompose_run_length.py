class Solution:
    def decompressRLElist(self, nums):
        new_list = []
        while nums:
            num = nums[:2]
            nums = nums[2:]
            for j in range(num[0]):
                new_list.append(num[1])
        return new_list


sol = Solution()
print(sol.decompressRLElist([1, 1, 2, 3]))
