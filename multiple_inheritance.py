class Parent1:
    def m1(self):
        print("parent 1 class method")


class Parent2:
    def m2(self):
        print("Parent 2 class Method")


class Child(Parent1, Parent2):
    def m3(self):
        print("Child class method")


if __name__ == '__main__':
    c = Child()
    c.m1()
    c.m2()
    c.m3()
