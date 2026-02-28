class Dog(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname=''):
        self.name=newname
dog = Dog(5)
dog.set_name("Aktos")
dog.set_age(6)
print(dog.get_age())
print(dog.get_name())
print(dog)
