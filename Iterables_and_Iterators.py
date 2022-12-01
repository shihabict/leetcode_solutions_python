from itertools import combinations


def iterables_and_iterators(s, k):
    count = 0
    combination = list(combinations(s, k))
    for com in combination:
        if 'a' in com:
            count += 1
    return format(count / len(combination), ".3f")


if __name__ == '__main__':
    num = int(input())
    s = ''.join(list(map(str, input().strip().split()))[:num])
    indx = int(input())
    print(iterables_and_iterators(s, indx))
