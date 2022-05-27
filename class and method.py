from datetime import date
class Person:#defining the class we are using
    def __init__(self,name,age):#the init method takes three objects
        self.name=name
        self.age=age
    
    @classmethod
    def fromBirthYear(cls,name,year):#defining the classmethod
        return cls(name,date.today().year-year)
    @staticmethod
    def isAdult(age):#defining the startic method
        return age>18#this returns boolean values
Person1=Person('charles',21)
Person2=Person.fromBirthYear('charles',1996)#assigning variables to the class but specifically to the class method

print(Person1.age)#printing out the age
print(Person2.age)

print(Person2.isAdult(22))#assigning variables to the class but specifically to the static method
