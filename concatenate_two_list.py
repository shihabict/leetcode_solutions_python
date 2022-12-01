def concatea_list(li1, li2):
    new_list = []
    if len(li1) == len(li2):
        for i, j in zip(li1, li2):
            new_list.append(i + j)
        return new_list
    else:
        print('List are of different length')


if __name__ == '__main__':
    print(concatea_list(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"]))
