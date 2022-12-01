class Solution:
    def convert(self, s, numRows):
        number_rows = {}
        for i in range(numRows):
            number_rows[i+1]=""

        counter = 1
        up = True

        for i in s:
            number_rows[counter]+=i
            if counter==1 or (counter<numRows and up):
                counter+=1
                up = True
            else:
                counter-=1
                up = False

        final_result = ''
        for row in range(numRows):
            final_result+=number_rows[row+1]
        return final_result



if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    sol.convert(s,numRows)