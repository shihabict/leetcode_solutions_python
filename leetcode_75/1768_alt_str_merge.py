class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        resulted_string = ""
        if len(word1) == len(word2):
            for i, j in zip(word1, word2):
                if i != " ":
                    resulted_string += i
                if j != " ":
                    resulted_string += j
        elif len(word1) != len(word2):
            if len(word1) > len(word2):
                word2 = word2 + " " * (abs(len(word1) - len(word2)))
                for i, j in zip(word1, word2):
                    if i != " ":
                        resulted_string += i
                    if j != " ":
                        resulted_string += j
            else:
                word1 = word1 + " " * (abs(len(word1) - len(word2)))
                for i, j in zip(word1, word2):
                    if i != " ":
                        resulted_string += i
                    if j != " ":
                        resulted_string += j
        return resulted_string.strip(" ")

if __name__ == '__main__':
    merge_alter = Solution()
    resulted_string = merge_alter.mergeAlternately("abc", "pqr")
    print(resulted_string)
