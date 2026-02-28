class Animal(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname=''):
        self.name=newname
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]
    def get_friends(self):
        return self.friends.copy()
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello")
    def age_diff(self,other):
        diff = self.get_age - other.get_age
        print(r"{abs(diff)} years of difference")
    def __str__(self):
        "person:"+str(self.name)+":"+str(self.age)

p1 = Person("Ali", 20)
p2 = Person("Tim", 15)
p1.age_diff(p2)