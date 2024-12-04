#python inheritance
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Create an instance of the Person class
x = Person("Suprekshya", "Karki")
x.printname()

#for the child class
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname,lname):
        Person. __init__(self,fname,lname)

x=Student("mike","tyson")
x.printname()  

#Add a property called graduationyear to the Student class:
#Add a year parameter, and pass the correct year when creating objects:
#Add a method called welcome to the Student class:
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
           print(self.firstname,self.lastname)
class Student(Person):
    def __init__ (self,fname,lname,year):
       super().__init__(fname,lname)
       self.graduationyear = year

    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of", self.graduationyear)

x=Student("suprekshya","karki",2024)
x.welcome()        