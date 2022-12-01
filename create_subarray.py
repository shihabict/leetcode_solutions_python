def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    print(lists)
    return max([sum(li) for li in lists]), list


# driver code
l1 = [-1, 4, 6, 8]
max_val, lis = sub_lists(l1)
print(max_val)
print(lis)
