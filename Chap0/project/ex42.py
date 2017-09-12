## Animal is-a object (yes, sort of confusing) look at the extra cred
class Animal(object):
    pass

## 定义继承自Animal的类Dog
class Dog(Animal):
    def __init__(self, name):
        ## 定义属性name并赋予初始值
        self.name = name

## define class inherit Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## difine class inherit object
class Person(object):

    def __init__(self, name):
        ## set the
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def sayname(self):
        print(self.name)

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## 调用父类的初始化函数，为继承的属性赋值
        super().__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

print(frank.name)
frank.sayname()
