def quicksort(l):
    '''recibe una l y la devuelve ordenada de menor a mayor'''
    if len(l) <= 1:
        return l
    pivote = l[0]
    l1 = []
    l2 = []
    for e in l[1:]:
        if e <= pivote:
            l1.append(e)
            continue
        l2.append(e)
    return quicksort(l1) + [pivote] + quicksort(l2)


print(quicksort([12, 654, 6, 8, 8, 48, 48, 489,
      48, 8, 5465, 15, 6165, 15, 1, 1, 1, 0]))
