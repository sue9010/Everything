
list = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]


def sort_item(list):
    t1, t2 = [], []
    for i in list:
        if i < 0:
            t1.append(i)
        else:
            t2.append(i)
    result = t1 + t2
    return result


print(sort_item(list))
