def remove_empty_string(li):
    while "" in li:
        li.remove("")
    return li

if __name__ == '__main__':
    print(remove_empty_string(["Mike", "", "Emma", "Kelly", "", "Brad"]))