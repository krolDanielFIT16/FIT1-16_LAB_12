import numpy


def sq_eq(a, b, c):
    D = (b**2 - 4 * a * c)**0.5
    x1 = (-b+D)/(2*a)
    x2 = (-b-D)/(2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")


def bsq_eq(a, b, c):
    D = (b**2 - 4 * a * c)**0.5
    x1 = ((-b + D) / (2 * a))**0.5
    x2 = ((-b - D) / (2 * a))**0.5
    print(f"x1 = {x1 if not numpy.iscomplex([x1])[0] else None}")
    print(f"x2 = {-x1 if not numpy.iscomplex([x1])[0] else None}")
    print(f"x3 = {x2 if not numpy.iscomplex([x2])[0] else None}")
    print(f"x4 = {-x2 if not numpy.iscomplex([x2])[0] else None}")


print("5x^2 + 8x + 2 = 0")
sq_eq(5, 8, 2)

print()

print("-5x^4 + 8x^2 + 2 = 0")
bsq_eq(-5, 8, 2)
