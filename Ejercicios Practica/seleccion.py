def seleccion(l):
    if len(l) <= 1:
        return l
    m = l[0]
    for e in l:
        if e < m:
            m = e
    l.remove(m)
    return [m] + seleccion(l)


print(seleccion([5, 8, 9, 7, 6, 4, 5, 2, 1, 5, 7, 1, 0]))
