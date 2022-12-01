def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    # return mergeTwoLists(left,right)
    mergeTwoLists(left, right, arr)


def mergeTwoLists(l1, l2, arr):
    # sorted_list = []
    i = j = k = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            # sorted_list.append(l1[i])
            arr[k] = l1[i]
            i += 1
        else:
            # sorted_list.append(l2[j])
            arr[k] = l2[j]
            j += 1
        k += 1

    return arr + l1[i:] + l2[j:]
    # arr + l1[i:] + l2[j:]


if __name__ == "__main__":
    arr = [2, 3, 1, 9, 2, 8, 64, 3, 56, 34]
    merge_sort(arr)
    print(arr)
