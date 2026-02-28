class Animal():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Class Animal: {self.name=}, {self.age=}"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


def make_animals(L1, L2):
    animals = []  # 1️⃣ бос тізім

    for i in range(len(L1)):  # 2️⃣ индекстермен жүру
        a = Animal(L1[i])     # 3️⃣ age беру
        a.set_name(L2[i])     # 4️⃣ name беру
        animals.append(a)    # 5️⃣ тізімге қосу

    return animals            # 6️⃣ тізімді қайтару

