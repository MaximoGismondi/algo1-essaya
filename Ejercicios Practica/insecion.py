
def insertion(l):
    if len(l) <= 1:
        return l
    return _insertion(l, 1)


def _insertion(l, i):
    if len(l) == i:
        return l

    n = i
    while l[n] < l[n-1] and n >= 1:
        l[n], l[n-1] = l[n-1], l[n]
        n -= 1

    return _insertion(l, i + 1)


print(insertion([10, 5, 8, 7, 1]))
