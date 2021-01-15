class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"name: {self.name}, ae:{self.age}, gender:{self.gender} I am eating")

    def drink(self):
        print(f"name: {self.name}, age:{self.age}, gender:{self.gender} I am drinking")

    def run(self):
        print(f"name: {self.name}, age:{self.age}, gender:{self.gender} I am runing")

xiaoming = Person("xiaomming", 10, "male")

xiaohong = Person("xiaohong", 12, "female")

print(xiaohong.name)

print(xiaoming.run())
