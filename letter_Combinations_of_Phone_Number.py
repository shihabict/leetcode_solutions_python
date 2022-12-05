class Solution:
    def letterCombinations(self, digits):
        number_char_dict = {'2':['a','b','c'],'3':['d','e','f']}
        for i in enumerate(digits)):
            for j in range(i,len(digits)):
                print()
        print('ok')


if __name__ == '__main__':
    digits = "23"
    sol = Solution()
    sol.letterCombinations(digits)