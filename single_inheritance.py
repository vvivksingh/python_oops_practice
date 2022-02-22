class Parent:
    a = 10

    def __init__(self):
        self.b = 20

    def m1(self):
        print("parent class instance method")

    @classmethod
    def m2(cls):
        print("Parent class method")

    @staticmethod
    def m3():
        print("Parent class static method")


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.d = 40

    def m4(self):
        print("Child Class Method")


if __name__ == '__main__':
    c = Child()
    c.m1()
    c.m2()
    c.m3()
    c.m4()
    print(c.d)
    print(c.a)
    print(c.b)
