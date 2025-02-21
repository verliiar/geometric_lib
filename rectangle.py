
def area_rectangle(a, b):
    if a >= 0 and b >= 0:
        return a * b
    return -1


def perimeter_rectangle(a, b, c, d):
    if a != 0 and b != 0 and c != 0 and d != 0:
        if (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
            return a + b + c + d
        else:
            return -1
    else:
        return 0
