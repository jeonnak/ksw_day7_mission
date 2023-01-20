# 10.1

class Thing():
    pass
print(Thing)

example = Thing()
print(example)

# 10.2

class Thing2():
    letters='abc'
print(Thing2.letters)

# 10.3

class Thing3():
    def __init__(self):
        self.letters='xyz'
example=Thing3()
print(example.letters)
