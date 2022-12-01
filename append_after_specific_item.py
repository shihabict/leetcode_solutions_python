def append_item_into_list(li, item1, item2):
    if item1 in li:
        index = li.index(item1)
        li = li.insert(index + 1, item2)
    return li


if __name__ == '__main__':
    print(append_item_into_list([10, 20, [300, 400, [5000, 6000], 500], 30, 40], 6000, 7000))
