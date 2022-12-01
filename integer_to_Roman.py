from collections import OrderedDict


class Solution:
    def intToRoman(self, s):

        rom_int_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                        "D": 500, "CM": 900, "M": 1000}
        int_value = 0
        prev_value = 0
        for i in s[::-1]:

            if rom_int_dict[i]:
                if prev_value!=0 and prev_value>rom_int_dict[i]:
                    int_value -= rom_int_dict[i]
                else:
                    int_value += rom_int_dict[i]
                prev_value = rom_int_dict[i]

        return int_value


if __name__ == '__main__':
    # num = 'LVIII'
    # num = 'MCMXCIV'
    num = 'III'
    sol = Solution()
    sol.intToRoman(num)
