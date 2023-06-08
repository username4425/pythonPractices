def func9(table):
    transparent = [[], [], [], []]
    print(transparent)
    for row in table:
        if row[3] is not None:
            if row[3] == "false":
                row[3] = "Не выполнено"
            else:
                row[3] = "Выполнено"
        if row[2] is not None:
            ds = row[2].split('-')
            row[2] = ds[2] + "." + ds[1] + "." + ds[0]
        if row[1] is not None:
            row[1] = "{:.4f}".format(float(row[1][:-1]) / 100)
        if row[0] is not None:
            pts = row[0].split(' ')
            row[0] = "(" + pts[1] + ") " + pts[2][:6] + "-" + pts[2][6:]
    table.sort(key=lambda a: a[2])
    table = table[::-1]
    for elems in table:
        for i, v in enumerate(elems):
            transparent[i].insert(0, v)
    return transparent