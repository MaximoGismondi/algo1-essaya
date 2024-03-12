def merge(lista1, lista2):
    if len(lista1) == 0:
        return lista2

    if len(lista2) == 0:
        return lista1

    if lista1[0] <= lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)

    return [lista2[0]] + merge(lista1, lista2[1:])


def mergesort(l):
    if len(l) <= 1:
        return l

    l1, l2 = l[:len(l)//2], l[len(l)//2:]
    return merge(mergesort(l1), mergesort(l2))


print(mergesort([3, 2, 1, 8, 7, 9, 5, 4, 6, 2,
      4, 6, 6, 8,  4, 5, 1, 1, 11, 1, 258]))
