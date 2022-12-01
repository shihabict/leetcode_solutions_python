def concatenate_two_lists_following_order(li1, li2):
    new_list = []
    if li1 and li2:
        for i in li1:
            for j in li2:
                new_list.append(i + j)
        return new_list
    else:
        print("List empty")


if __name__ == '__main__':
    print(concatenate_two_lists_following_order(["Hello ", "take "], ["Dear", "Sir"]))
