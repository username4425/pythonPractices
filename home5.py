from re import findall


def func8(s):
    return findall(r"\[\s?make\s?@'([\w\d]+)'\s?<=\s?@\"([\w\d]+)\"\.\s?\]", s)
