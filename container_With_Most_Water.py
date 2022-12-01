class Solution:
    def maxArea(self, height):
        res = 0
        left_p_indx = 0
        right_p_indx = len(height) - 1

        loop_trun = True
        while loop_trun:
            left_p = height[left_p_indx]
            right_p = height[right_p_indx]
            area = (right_p_indx - left_p_indx) * min(left_p, right_p)
            res = max(area,res)
            if right_p_indx==left_p_indx:
                loop_trun = False
            elif left_p>right_p:
                right_p_indx-=1
            else:
                left_p_indx+=1
        return res

        # Brute force
        # p = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j-i)*min(height[i], height[j])
        #         p = max(p, area)
        # return p


if __name__ == '__main__':
    heigth = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    result = sol.maxArea(heigth)
    print(result)
