def binary_search(list, indx):
    left_index = 0
    right_index = len(list) - 1
    # mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = list[mid_index]
        if mid_number == indx:
            return mid_index
        elif mid_number < indx:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


def binary_recursion(num_list, itm, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(num_list) or mid_index < 0:
        return -1
    mid_number = num_list[mid_index]
    if mid_number == itm:
        return mid_index
    elif mid_number < itm:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_recursion(num_list, itm, left_index, right_index)


if __name__ == '__main__':
    li = [1, 2, 3, 4, 56, 789, 790]
    # print(binary_search(li, 56))
    print(binary_recursion(li, 889, 0, len(li)))
