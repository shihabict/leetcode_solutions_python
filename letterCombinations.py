class Solution:
    def letterCombinations(self, digits):
        letter_digit_comb = []
        digit_letter_dict = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'],
                             "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'],
                             "9": ['w', 'x', 'y', 'z']}
        if len(digits) == 1:
            return digit_letter_dict[digits]
        if len(digits) == 2:
            li_1 = digit_letter_dict[digits[0]]
            li_2 = digit_letter_dict[digits[1]]
            for i in range(len(li_1)):
                for j in range(len(li_2)):
                    letter_digit_comb.append(li_1[i] + li_2[j])

        if len(digits) == 3:
            li_1 = digit_letter_dict[digits[0]]
            li_2 = digit_letter_dict[digits[1]]
            li_3 = digit_letter_dict[digits[2]]
            for i in range(len(li_1)):
                for j in range(len(li_2)):
                    for k in range(len(li_3)):
                        letter_digit_comb.append(li_1[i] + li_2[j] + li_3[k])
        if len(digits) == 4:
            li_1 = digit_letter_dict[digits[0]]
            li_2 = digit_letter_dict[digits[1]]
            li_3 = digit_letter_dict[digits[2]]
            li_4 = digit_letter_dict[digits[3]]
            for i in range(len(li_1)):
                for j in range(len(li_2)):
                    for k in range(len(li_3)):
                        for r in range(len(li_4)):
                            letter_digit_comb.append(li_1[i] + li_2[j] + li_3[k] + li_4[r])
        return letter_digit_comb


if __name__ == '__main__':
    digits = "23"
    sol = Solution()
    res = sol.letterCombinations(digits)
    print(res)
