### class ###
class SmartPhone:
    # contructor
    def __init__(self, device, brand):
        self.device = device
        self.brand = brand

    def description(self):
        return f'{self.device} of {self.brand} supports android 14'


phoneObj = SmartPhone("Smartphone", "Samsung")
print(phoneObj.description())


### inheritance ###
#!/usr/bin/python
# define parent class
class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Calling from chold. Parent attribute :", Parent.parentAttr)

    def sum(self, a, b):
        return a + b

# define child class


class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

    def sum(self, a, b):
        return a + b + 10


# instance of child
c = Child()
# child calls its method
c.childMethod()
# calls parent's method
c.parentMethod()
# again call parent's method
c.setAttr(200)
# again call parent's method
c.getAttr()
print(c.sum(10, 10))


class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    @classmethod
    def showcount(cls):
        print (cls.empCount)

    @classmethod
    def newemployee(cls, name, age):
        return cls(name, age)

e1 = Employee("Bhavana", 24)
e2 = Employee("Rajesh", 26)
e3 = Employee("John", 27)
e4 = Employee.newemployee("Anil", 21)

Employee.showcount()


class Employee2:
   def __init__(self, name, age, salary):
      self.name = name # public variable
      self.__age = age # private variable
      self._salary = salary # protected variable
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.__age, ", salary: ", self._salary)

e1=Employee2("Bhavana", 24, 10000)

print (e1.name)
print (e1._salary)
#print (e1.__age)


### abstract classes ###
from abc import ABC, abstractmethod
class democlass(ABC):
   @abstractmethod
   def method1(self):
      print ("abstract method")
      return
   def method2(self):
      print ("concrete method")

class concreteclass(democlass):
   def method1(self):
      super().method1()
      return
      
obj = concreteclass()
obj.method1()
obj.method2()



class Thermostat:
    def __init__(self, celsius):
        self._celsius = celsius  # Internal "private" attribute

    @property
    def temperature(self):
        """The getter: returns the current temperature."""
        return self._celsius

    @temperature.setter
    def temperature(self, value):
        """The setter: adds validation before updating."""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

# Usage
t = Thermostat(25)
print(t.temperature)   # Triggers getter -> 25
t.temperature = 30     # Triggers setter
# t.temperature = -300 # Would raise ValueError