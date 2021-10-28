




def find_smallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c


res1 = find_smallest(5, 78, 12)
print(res1)