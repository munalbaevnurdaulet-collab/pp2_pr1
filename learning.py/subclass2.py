class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def set_name(self,newname=""):
        self.name=newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends.copy()

import random 
class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major=major
    def change_major(self,major):
        self.major=major
    def speak(self):
        r = random.random()
        if r<0.25:
            print("i have homework")
        elif 0.25<=r<0.5:
            print("i need sleep")
        elif 0.5<=r<0.75:
            print("I should eat")
        else:
            print("I'm still zooming")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

s = Student("Ali", 18, "CS")
print(s)

