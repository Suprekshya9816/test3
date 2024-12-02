
bottle = "paani"
age = 22

  #printing
print(f"Bottle contains {bottle} ")
print(bottle)

 #list
fruit1 = "apple"
fruit2 = "banana"
fruit3 = "guava"

fruits =["apple","banana","guava"]
print(fruits[0])
print(fruits[2])
print(fruits[-1]) #last Item
print(fruits[0:3]) #range
print(len(fruits)) # calculate length of list
  

fruits.append("mango") # add to ythe last index of list
print (fruits)
fruits.pop() #last bata nikalni
print(fruits)



fruits.insert(3, "orange") #insert le aafulai required thau ma item add garna milaxa.
print(fruits)

#dictionary

me={
    "fruits":"yavaguard",
    "age": 22
}
me["address"]= "Itahari" #dictionary ma add garxa
print(me)
print(me["age"])
del me['age']#delete
print(me.keys())
print(me.values())

#Distionary(clear)

car = {
"brand":"hihi",
"year":1997,
"model":"abc"

}
car.clear()
print(car)

#copy
fruits = {
"Brand":"mustang",
"model":"applicable",
"year": 9999
}
fruits.copy()
print(fruits)

#get
car={
"model":"abs",
"year": 1234,
"brand":"applicable"
}
x=car.get("brand")
print(x)

#items
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

#create object
class escope:
  x=8

#create object
class MyClass:
  x = 6

p1 = MyClass()
print(p1.x)

class student:
  x=3

p1 = student()
print(p1.x)  

#_init_() Function

class Animal:
  def __init__(self,brand,species):
    self.brand = brand
    self.species = species

A1 = Animal("abc","vastigo")

print(A1.brand)
print(A1.species)

class Shoes:
  def __init__(self,name,brand):
    self.name =  name
    self.brand = brand

S1 = Shoes("jbell","Gitts")   
print(S1.name) 
print(S1.brand)

#_STR_
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)