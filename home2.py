def func6(x):
    tree = {
        2015: {
            'i': 2,
            1961: 9,
            1967: {
                'i': 4,
                'METAL': 0,
                'PUG': {
                    'i': 1,
                    1983: 1,
                    1962: 2,
                    2012: 3
                },
                'STAN': 4
            },
            2003: {
                'i': 0,
                'HTTP': {
                    'i': 1,
                    1983: 5,
                    1962: 6,
                    2012: 7
                },
                'MASK': 8
            }
        },
        2016: 10,
        2001: 11
    }
    i = 3
    while True:
        node = tree.get(x[i])
        if type(node) == int:
            return node
        i = node['i']
        tree = node


def func7(s):
    b = int(s, base=16)
    j4 = (b & 0b111111111000000000000000) >> 3
    j3 = (b & 0b000000000111000000000000) << 9
    b &= 0b000000000000000000011111
    b |= j3
    b |= j4
    return hex(b)

