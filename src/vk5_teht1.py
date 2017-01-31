def luvut(b):
    k = 0
    a = []
    a.append(1)
    while a[k] <= b:
        a.append(a[k] * 2)
        k += 1

    return a

print luvut(13)
