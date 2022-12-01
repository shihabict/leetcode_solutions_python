def bubble_sort(elements):
    for i in range(len(elements)):
        swaped = False
        for j in range(len(elements) - 1 - i):
            if elements[i] > elements[i + 1]:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
                swaped = True
        if swaped:
            break
    return elements


if __name__ == '__main__':
    elements = [3, 2, 75, 34, 64]
    print(bubble_sort(elements))
