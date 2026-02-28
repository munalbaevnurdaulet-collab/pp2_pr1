"""class travel(object):
    def __init__(self,city1,city2,car):
        self.city1=city1
        self.city2=city2
        self.car = car
    def __str__(self):
        return "I'm going to the " +str(self.city2)+" from the " + str(self.city1) + " by our car " + str(self.car)
travel = travel("Aktau","Almaty","Toyota land cruiser 100")
print(travel)"""
"""
class Animals(object):
    def __init__(self,age):
        self.age=age
        self.name=None

    def __str__(self):
        return f"animal:{self.name}:{self.age}"

def make_animals(L1,L2):
    result=[]
    for age, name in zip(L1,L2):
        a = Animals(age)
        a.name=name
        result.append(a)
    return result

L1 = [2,5,1]
L2 = ["Rex", "Laika", "Gans"]

animals = make_animals(L1,L2)

print(animals)
for i in animals:
    print(i)"""

a = int(input())
if a>=100:
    print("Molodes")
else:
    print("Chort  loh  dolboeb ")