from struct import unpack


def func11(data):
    struct_a = unpack(">IHccIdHHHQ", data[4:38])
    A = {}
    b = []
    b_arr_size = struct_a[0]
    b_arr_address = struct_a[1]
    for i in range(b_arr_size):
        b_addr = unpack(">H", data[b_arr_address: b_arr_address + 2])[0]
        b_struct = unpack(">qi", data[b_addr: b_addr + 12])
        b.append({"B1": b_struct[0], "B2": b_struct[1]})
        b_arr_address += 2
    A["A1"] = b
    A["A2"] = (struct_a[2] + struct_a[3]).decode("ascii")
    struct_c = unpack(">bbbbbbbbIIIIh", data[struct_a[4]: struct_a[4] + 26])
    A["A3"] = {"C1": list(struct_c[:8]), "C2": list(struct_c[8:12]),
               "C3": struct_c[12]}
    A["A4"] = struct_a[5]
    A["A5"] = list(
        unpack(
            ">" + "q" * struct_a[6],
            data[struct_a[7]: struct_a[7] + struct_a[6] * 8]
        )
    )
    struct_d = unpack(">qf", data[struct_a[8]: struct_a[8] + 12])
    A["A6"] = {"D1": struct_d[0], "D2": struct_d[1]}
    A["A7"] = struct_a[-1]
    result = "{'A1': [" + ",\n        ".join(map(lambda a: str(a), A["A1"])) \
             + "],\n"
    result += "'A2': {},\n".format(A['A2'])
    result += "'A3': {{'C1': {},\n       'C2': {},\n       'C3': {}}},\n". \
        format(A["A3"]["C1"], A["A3"]["C2"], A["A3"]["C3"])
    result += "'A4': {},\n".format(A["A4"])
    result += "'A5': {},\n".format(A["A5"])
    result += "'A6': {},\n".format(A["A6"])
    result += "'A7': {}}}".format(A["A7"])
    return result
