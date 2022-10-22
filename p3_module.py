def area(r1, r2, h):
    l = ((r2 - r1) ** 2 + h ** 2) ** 0.5
    return 3.14 * l * (r1 + r2)


def volume(r1, r2, h):
    return 1 / 3 * 3.14 * h * (r1 ** 2 + r1 * r2 + r2 ** 2)
