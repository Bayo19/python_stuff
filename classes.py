class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def addition(self):
        return self.r + self.i


x = Complex(15, 12)

print(x.addition())

# corey schafer
class Employee:

    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def info(self):
        return '{}-{}-{}'.format(self.first, self.last, self.pay)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)





emp_1 = Employee('Johnny', 'Blair', 45000)
emp_2 = Employee('Bayo', 'Ade', 90000)
# print(emp_2.info())
emp_2.raise_amount = 1.05
emp_2.apply_raise()
# print(emp_2.info())
print(emp_2.__dict__)

# class variables - shared amongst all instances of a class