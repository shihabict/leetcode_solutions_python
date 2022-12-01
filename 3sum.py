# def printCombination(arr, n, r):
#     data = [0] * r
#
#     # Print all combination
#     # using temporary array 'data[]'
#     combinationUtil(arr, data, 0,
#                     n - 1, 0, r)
#
#
# def combinationUtil(arr, data, start,
#                     end, index, r):
#     if (index == r):
#         for j in range(r):
#             print(data[j], end=" ")
#         print()
#         return
#
#     i = start
#     while (i <= end and end - i + 1 >= r - index):
#         data[index] = arr[i]
#         combinationUtil(arr, data, i + 1,
#                         end, index + 1, r)
#         i += 1

def three_sum(arr):
    import itertools
    arr_list = list(itertools.combinations(arr, 3))
    return [ar_ for ar_ in arr_list if sum(ar_)==0]
# Driver Code
arr = [-1, 0, 1, 2, -1, -4]
r = 3
n = len(arr)
# printCombination(arr, n, r)
print(three_sum(arr))

# # This code is contributed by mits
# arr = [-1, 0, 1, 2, -1, -4]
# # arr = [0,1,1]
# # arr = [1, 2, 3]
# print(sub_lists(arr))

# print(sub_arrays(arr, k = 3)) # size = 2
