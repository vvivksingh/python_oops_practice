class Parent:
    def m1(self):
        print("Parent class Method")


class Child1(Parent):
    def m2(self):
        print("Child 1 class method")


class Child2(Parent):
    def m3(self):
        print("Child 2 class method")


if __name__ == '__main__':
    c1 = Child1()
    c1.m1()
    c1.m2()
    # c1.m3() --> This will not work
    c2 = Child2()
    c2.m1()
    c2.m3()
    # c2.m2 --> This will not work
