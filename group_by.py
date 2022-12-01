from itertools import groupby


def compress_the_string(s):
    li = [list(g) for k, g in groupby(s)]

    for element in li:
        print(tuple((len(element), int(element[0]))), end=' ')

if __name__ == '__main__':
    s = input()
    compress_the_string(s)
