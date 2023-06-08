class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name
        super().__init__(method_name)


class AAMiles:
    def __init__(self):
        self.state = 0
        self.transition_table = [
            {"init": [1, 0], "coat": [3, 1]},
            {"init": [2, 2], "coat": [7, 3]},
            {"coat": [3, 4]},
            {"crush": [4, 5]},
            {"coat": [5, 6]},
            {"coat": [2, 8], "fork": [6, 7]},
            {"coat": [7, 9], "fork": [3, 10]},
            {"crush": [2, 11]}
        ]

    def run(self, name):
        if name in self.transition_table[self.state]:
            val = self.transition_table[self.state][name][1]
            self.state = self.transition_table[self.state][name][0]
            return val
        else:
            raise MealyError(name)

    def init(self):
        return self.run("init")

    def coat(self):
        return self.run("coat")

    def crush(self):
        return self.run("crush")

    def fork(self):
        return self.run("fork")


def main():
    return AAMiles()


def test():
    o = main()  # A
    o.init()  # B
    o.coat()  # H
    o.crush()  # C
    o.coat()  # D
    o.crush()  # E
    try:
        o.fork()
    except MealyError:
        pass
    try:
        o.init()
    except MealyError:
        pass
    try:
        o.crush()
    except MealyError:
        pass
    o.coat()   # F
    try:
        o.crush()
    except MealyError:
        pass
    try:
        o.init()
    except MealyError:
        pass
    o.coat()  # C
    o.coat()  # D
    o.crush()  # E
    o.coat()  # F
    o.fork()  # G
    try:
        o.init()
    except MealyError:
        pass
    try:
        o.crush()
    except MealyError:
        pass
    o.fork()  # D
    o.crush()  # E
    o.coat()  # F
    o.fork()  # G
    o.coat()  # H
    o = main()  # A
    o.coat()  # D
    o = main()  # A
    o.init()  # B
    o.init()  # C
