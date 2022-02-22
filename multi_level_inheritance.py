class Parent:
    def m1(self):
        print("Parent class method")


class Child(Parent):
    def m2(self):
        print("Child class method")


class GrandChild(Child):
    def m3(self):
        print("Grand Child class")


if __name__ == '__main__':
    gc = GrandChild()
    gc.m1()
    gc.m2()
    gc.m3()
