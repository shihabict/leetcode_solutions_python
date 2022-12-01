
from collections import OrderedDict


class Solution:
    def intToRoman(self, num):
        rom_int_dict = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
                        "D": 500, "CM": 900, "M": 1000}
        reverse_dict = OrderedDict(reversed(list(rom_int_dict.items())))
        roman_digit = ''

        for i in reverse_dict:
            int_value = num // reverse_dict[i]
            if int_value > 0:
                roman_digit += (int_value * i)
            num = num % reverse_dict[i]

        return roman_digit


if __name__ == '__main__':
    # num = 3
    # num = 58
    num = 1994
    sol = Solution()
    sol.intToRoman(num)

class Solution:
    def romanToInt(self, s: str) -> int:
        result, prev = 0, 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:  # rev the s
            if dict[i] >= prev:
                result += dict[i]
            else:
                result -= dict[i]
            prev = dict[i]
        return result


sol = Solution()
print(sol.romanToInt('LVIII'))

