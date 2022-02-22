# parent class
class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print("Employee Name: ", self.name)
        print("Employee Id: ", self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber, )

    def employee_info(self):
        a.display()

        print("Employee salary: ", self.salary)
        print("Employee post: ", self.post)


# creation of an object variable or an instance
a = Employee('Vivek', 1001, 20000, "Intern")

if __name__ == '__main__':
    # calling a function of the class Person using its instance
    a.employee_info()
