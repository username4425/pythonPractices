import math


def func1(z):
    return (30 * (1 - z - z ** 3) ** 6 - z ** 3) / (18 * z ** 7 + 15 * z ** 2 - 87 - 42 * z ** 3) - \
           math.sqrt(z ** 4 / 21 / z ** 4)


def func2(x):
    if (x < 48):
        return 29 - (18 * x) ** 3
    elif (x < 102):
        return 66 * (x ** 2 / 35 + 50 * x) + (14 * x ** 2 - x ** 3) ** 6
    else:
        return 22 * math.cos(73 - 34 * x ** 2 - 70 * x) + (x ** 3 + x ** 2 + x) ** 5


def func3(b, n, m):
    sum = 0
    for k in range(1, m + 1):
        for i in range(1, n + 1):
            for j in range(1, b + 1):
                sum += 78 * (k ** 3 - k - j ** 2) ** 6 - 55 * i
    return sum


def func4(n):
    if n == 0:
        return -0.8
    if n == 1:
        return 0.96
    return 18 * math.floor(main(n - 2)) - math.atan(main(n - 1) ** 3 / 71 + 1) ** 3 - 58


def func5(z):
    sum = 0
    n = len(z)
    for i in range(1, n + 1):
        sum += 53 * (z[n - math.ceil(i / 4)] ** 2 - 5 * z[i - 1] ** 3
                     - 59 * z[n - math.ceil(i / 4)]) ** 4
    return sum

