import re


def start_end(s, k):
    exist = re.search(k, s)
    pattern = re.compile(k)
    if not exist: print("(-1, -1)")
    while exist:
        print("({0}, {1})".format(exist.start(), exist.end() - 1))
        exist = pattern.search(s, exist.start() + 1)


if __name__ == '__main__':
    s = input()
    k = input()
    start_end(s, k)



