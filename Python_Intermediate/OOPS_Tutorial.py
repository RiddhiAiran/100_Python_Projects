from logging import lastResort


class Employee:

    raise_amount = 1.04
    total_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@company.com'
        self.pay = pay

        Employee.total_employee += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amount)



emp_01 = Employee("Riddhi","Gupta", 50000)
emp_02 = Employee('Siddhi','Gupta',42000)
print(emp_02.pay)
emp_02.raise_pay()
print(emp_02.pay)

print(Employee.total_employee)